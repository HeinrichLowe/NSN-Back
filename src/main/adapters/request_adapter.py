from fastapi import Request
from pydantic import BaseModel
from src.presentation.http_types import HttpRequest, HttpResponse
from src.presentation.interfaces.controller_interface import IController

async def request_adapter(request: Request, controller: IController, schema: type[BaseModel] = None) -> HttpResponse:
    body_data = None
    if await request.body():
        body = await request.json()

        if schema:
            body_data = schema(**body).model_dump()
        else:
            body_data = body

    http_request = HttpRequest(
        headers=request.headers,
        query_params=request.query_params,
        path_params=request.path_params,
        body=body_data,
        url=str(request.url)
    )

    http_response = await controller.handle(http_request)
    return http_response
