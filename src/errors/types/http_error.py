class HttpError(Exception):
    status_code: int
    name: str
    message: str

    def __init__(self, message: str = None):
        self.message = message or self.message
