from passlib.hash import pbkdf2_sha256
from decouple import config
from src.presentation.interfaces.controller_interface import IController
from src.domain.use_cases.user.signup import ISignup
from src.domain.entities.user import User
from src.presentation.http_types import HttpRequest, HttpResponse

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRATION = config('ACCESS_TOKEN_EXPIRATION')
REFRESH_TOKEN_EXPIRATION = config('REFRESH_TOKEN_EXPIRATION')
Sha = pbkdf2_sha256

class SignupController(IController):
    def __init__(self, use_case: ISignup) -> None:
        self.__use_case = use_case

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        request = http_request.body

        response = await self.__use_case.execute(User(
            email=request["email"],
            username=request["username"].lower() if request["username"] else None,
            password=Sha.hash(request["password"]),
            full_name=request["full_name"],
            birth_date=request["birth_date"]
        ))

        return  HttpResponse(
            status_code=201,
            body={ "data": response }
        )
