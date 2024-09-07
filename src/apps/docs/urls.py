from django.urls import path
from drf_spectacular import views, utils

urlpatterns = [
    path(
        "api/v1/schema/",
        utils.extend_schema(exclude=True)(views.SpectacularAPIView).as_view(),
        name="schema",
    ),
    path(
        "docs/",
        utils.extend_schema(exclude=True)(views.SpectacularSwaggerView).as_view(
            url_name="schema"
        ),
        name="swagger-ui",
    ),
    path(
        "redoc/",
        utils.extend_schema(exclude=True)(views.SpectacularRedocView).as_view(
            url_name="schema"
        ),
        name="redoc",
    ),
]
