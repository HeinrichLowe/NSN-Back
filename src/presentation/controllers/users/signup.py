from src.presentation.interfaces.controller_interface import IController
from src.domain.use_cases.user.signup import ISignup
from src.domain.entities.user import User
from src.presentation.http_types import HttpRequest, HttpResponse

class SignupController(IController):
    def __init__(self, use_case: ISignup) -> None:
        self.__use_case = use_case

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        request = http_request.body

        response = await self.__use_case.execute(User(
            email=request["email"],
            username=request["username"].lower() if request["username"] else None,
            password=request["password"],
            full_name=request["full_name"],
            birth_date=request["birth_date"]
        ))

        return  HttpResponse(
            status_code=201,
            body=response
        )
