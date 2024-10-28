from src.presentation.http_types.http_response import HttpResponse
from .types import HttpError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": {
                    "title": error.name,
                    "datail": error.message
                }
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": {
                "title": "Internal Server Error",
                "datail": str(error)
            }
        }
    )
