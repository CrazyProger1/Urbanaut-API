from rest_framework import authentication


class APIKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        pass
