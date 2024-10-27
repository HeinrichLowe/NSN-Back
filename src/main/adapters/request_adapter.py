from fastapi import Request
from src.presentation.http_types import HttpRequest, HttpResponse
from src.presentation.interfaces.controller_interface import IController

async def request_adapter(request: Request, controller: IController) -> HttpResponse:
    body = None
    if await request.body():
        body = await request.json()

    http_request = HttpRequest(
        headers=request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        body=body,
        url=str(request.url)
    )

    http_response = await controller.handle(http_request)
    return http_response
