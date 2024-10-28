from .http_error import HttpError

class HttpUnprocessableEnttityError(HttpError):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'Unprocessable Entity'
        self.status_code = 422
