from drf_spectacular.extensions import OpenApiAuthenticationExtension


class TMAAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = "src.apps.accounts.backends.TMAAuthentication"
    name = "Telegram Mini Apps"

    def get_security_definition(self, auto_schema):
        return {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Telegram-Mini-Apps authentication using an Authorization header.",
        }
