class InvalidWebsocketTokenError(Exception):
    def __init__(self, message: str, token: str) -> None:
        self.message = message
        self.token = token
        super().__init__(message)
