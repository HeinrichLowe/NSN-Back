from passlib.hash import pbkdf2_sha256
from decouple import config
from src.presentation.interfaces.controller_interface import IController
from src.domain.use_cases.user.signin import ISignIn
from src.domain.entities.user import User
from src.presentation.http_types import HttpRequest, HttpResponse

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRATION = config('ACCESS_TOKEN_EXPIRATION')
REFRESH_TOKEN_EXPIRATION = config('REFRESH_TOKEN_EXPIRATION')
Sha = pbkdf2_sha256

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
            body={ "data": response }
        )
