from src.presentation.http_types.http_response import HttpResponse
from .types import HttpBadRequestError, HttpNotFoundError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpBadRequestError)):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "error": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "error": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )

