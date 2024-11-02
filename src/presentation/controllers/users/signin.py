from src.presentation.interfaces.controller_interface import IController
from src.domain.use_cases.user.signin import ISignIn
from src.domain.entities.user import User
from src.presentation.http_types import HttpRequest, HttpResponse

class SigninController(IController):
    def __init__(self, use_case: ISignIn) -> None:
        self.__use_case = use_case

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        request = http_request.body

        response = await self.__use_case.execute(User(
            email=request["email"] if request["email"] else None,
            username=request["username"].lower() if request["username"] else None,
            password=request["password"]
        ))

        return  HttpResponse(
            status_code=200,
            body=response
        )
