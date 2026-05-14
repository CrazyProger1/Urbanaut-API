from datetime import timedelta

import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import exceptions
from rest_framework.test import APIRequestFactory

from src.apps.external.authentications import HMACAuthentication
from src.apps.external.models import Application, Key
from src.utils.django.hmac import get_signature

User = get_user_model()


@pytest.fixture
def factory():
    return APIRequestFactory()


@pytest.fixture
def auth():
    return HMACAuthentication()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        email="hmac-tester@example.com",
        password="irrelevant",
    )


@pytest.fixture
def application(user):
    return Application.objects.create(name="test-app", created_by=user)


@pytest.fixture
def key(application, user):
    return Key.objects.create(
        application=application,
        created_by=user,
        name="test-key",
        expired_at=timezone.now() + timedelta(days=1),
    )


def _build_request(factory, key: Key, *, method="POST", path="/api/test/", payload=None):
    payload = payload if payload is not None else {"hello": "world"}
    request = getattr(factory, method.lower())(path, payload, format="json")
    signature = get_signature(
        key=key.key,
        method=method,
        url=request.build_absolute_uri(),
        payload=request.body,
    )
    request.META["HTTP_X_API_KEY"] = str(key.pk)
    request.META["HTTP_X_API_SIGNATURE"] = signature.hex()
    return request


@pytest.mark.django_db
def test_authenticate_success(factory, auth, key, user):
    request = _build_request(factory, key)

    result = auth.authenticate(request)

    assert result is not None
    authenticated_user, authenticated_key = result
    assert authenticated_user == user
    assert authenticated_key == key


@pytest.mark.django_db
def test_authenticate_missing_key_header_returns_none(factory, auth, key):
    request = _build_request(factory, key)
    del request.META["HTTP_X_API_KEY"]

    assert auth.authenticate(request) is None


@pytest.mark.django_db
def test_authenticate_missing_signature_header_returns_none(factory, auth, key):
    request = _build_request(factory, key)
    del request.META["HTTP_X_API_SIGNATURE"]

    assert auth.authenticate(request) is None


@pytest.mark.django_db
def test_authenticate_no_headers_returns_none(factory, auth):
    request = factory.post("/api/test/", {"hello": "world"}, format="json")

    assert auth.authenticate(request) is None


@pytest.mark.django_db
def test_authenticate_unknown_key(factory, auth, key):
    request = _build_request(factory, key)
    request.META["HTTP_X_API_KEY"] = "00000000-0000-0000-0000-000000000000"

    with pytest.raises(exceptions.AuthenticationFailed, match="Key not found"):
        auth.authenticate(request)


@pytest.mark.django_db
def test_authenticate_expired_key(factory, auth, key):
    key.expired_at = timezone.now() - timedelta(seconds=1)
    key.save(update_fields=["expired_at"])

    request = _build_request(factory, key)

    with pytest.raises(exceptions.AuthenticationFailed, match="Key expired"):
        auth.authenticate(request)


@pytest.mark.django_db
def test_authenticate_revoked_key(factory, auth, key):
    key.is_revoked = True
    key.save(update_fields=["is_revoked"])

    request = _build_request(factory, key)

    with pytest.raises(exceptions.AuthenticationFailed, match="Key is revoked"):
        auth.authenticate(request)


@pytest.mark.django_db
def test_authenticate_invalid_signature(factory, auth, key):
    request = _build_request(factory, key)
    request.META["HTTP_X_API_SIGNATURE"] = "tampered-signature"

    with pytest.raises(exceptions.AuthenticationFailed, match="Request lost integrity"):
        auth.authenticate(request)


@pytest.mark.django_db
def test_authenticate_signature_bound_to_payload(factory, auth, key):
    request = _build_request(factory, key, payload={"hello": "world"})
    other_signature = get_signature(
        key=key.key,
        method="POST",
        url=request.build_absolute_uri(),
        payload=b'{"hello":"tampered"}',
    )
    request.META["HTTP_X_API_SIGNATURE"] = other_signature.decode("latin-1")

    with pytest.raises(exceptions.AuthenticationFailed, match="Request lost integrity"):
        auth.authenticate(request)