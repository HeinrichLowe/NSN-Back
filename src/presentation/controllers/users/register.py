from passlib.hash import pbkdf2_sha256
from decouple import config
from src.presentation.interfaces.controller_interface import IController
from src.domain.use_cases.user_register import IUserRegister
from src.domain.entities.user import User
from src.presentation.http_types import HttpRequest, HttpResponse

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRATION = config('ACCESS_TOKEN_EXPIRATION')
REFRESH_TOKEN_EXPIRATION = config('REFRESH_TOKEN_EXPIRATION')
Sha = pbkdf2_sha256

class RegisterController(IController):
    def __init__(self, use_case: IUserRegister) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        request = http_request.body

        response = self.__use_case.register(User(
            email=request["user"]["email"],
            username=request["user"]["username"].lower() if request["user"]["username"] else None,
            password=Sha.hash(request["user"]["password"]),
            full_name=request["user"]["full_name"],
            birthday=request["user"]["birthday"]
        ))

        return  HttpResponse(
            status_code=200,
            body={ "data": response }
        )
