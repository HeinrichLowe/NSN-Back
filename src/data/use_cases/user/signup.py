import re
from typing import Dict
from passlib.hash import pbkdf2_sha256 as Sha
from src.domain.entities.user import User
from src.domain.use_cases.user.signup import ISignup
from src.domain.use_cases.user.token_generator import ITokenGenerator
from src.data.interfaces.user_repository import IUserRepository
from src.errors.types import HttpBadRequestError

class Signup(ISignup):
    def __init__(self, repository: IUserRepository, token_generator: ITokenGenerator):
        self.__repository = repository
        self.__token_generator = token_generator

    async def execute(self, user: User) -> Dict:
        if user.username:
            self.__validate_username(user.username)
            await self.__checks_for_duplicate_username(user.username)

        if user.email:
            self.__validate_email(user.email)
            await self.__checks_for_duplicate_email(user.email)

        self.__validate_name(user.full_name)
        user.password = Sha.hash(user.password)

        response = await self.__registry_user_info(user)
        tokens = await self.__token_generator.create_tokens(response)
        return self.__format_response(tokens)

    @classmethod
    def __validate_username(cls, username: str) -> None:
        if not re.match("^[a-zA-Z0-9_]+$", username):
            raise HttpBadRequestError('Invalid username.')

        if len(username) > 16:
            raise HttpBadRequestError('Username to long.')

    async def __checks_for_duplicate_username(self, username: str):
        response = await self.__repository.find_by_username(username)
        if response is not None:
            raise HttpBadRequestError("That username is already in use. Please try a different one.")

    @classmethod
    def __validate_email(cls, email: str) -> None:
        if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
            raise HttpBadRequestError('Invalid email.')

    async def __checks_for_duplicate_email(self, email: str):
        response = await self.__repository.find_by_email(email)
        if response is not None:
            raise HttpBadRequestError("That email is already in use. Please try a different one.")

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not re.match("^[a-zA-Z ]+$", name):
            raise HttpBadRequestError('Invalid name.')

        if len(name) > 32:
            raise HttpBadRequestError('Name to long.')

        if not name:
            raise HttpBadRequestError('Name is required.')

    async def __registry_user_info(self, user: User) -> User:
        return await self.__repository.signup(user)

    @classmethod
    def __format_response(cls, tokens: Dict) -> Dict:
        return { **tokens }
