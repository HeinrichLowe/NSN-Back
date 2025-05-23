from src.presentation.interfaces.controller_interface import IController
from src.domain.use_cases.user.search_by_name import ISearchByName
from src.presentation.http_types import HttpRequest, HttpResponse

class SearchByNameController(IController):
    def __init__(self, use_case: ISearchByName) -> None:
        self.__use_case = use_case

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.query_params["name"]

        response = await self.__use_case.find(name)

        return  HttpResponse(
            status_code=200,
            body=response
        )
