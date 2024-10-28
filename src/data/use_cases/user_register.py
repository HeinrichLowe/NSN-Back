from typing import Dict
import re
from src.domain.use_cases.user_register import IUserRegister
from src.domain.entities.user import User
from src.data.interfaces.user_repository import IUserRepository
from src.errors.types import HttpBadRequestError

class UserRegister(IUserRegister):
    def __init__(self, repository: IUserRepository):
        self.__repository = repository

    async def register(self, user: User) -> Dict:
        self.__validate_name(user.full_name)
        self.__validate_username(user.username)
        await self.__checks_for_duplicate_username(user.username)

        response = await self.__registry_user_info(user)
        return self.__format_response(response)

    async def __checks_for_duplicate_username(self, username: str):
        response = await self.__repository.search_by_username(username)
        if response is not None:
            raise HttpBadRequestError("User already exists.")

    @classmethod
    def __validate_username(cls, username: str) -> None:
        if not re.match("^[a-zA-Z0-9_]+$", username):
            raise HttpBadRequestError('Invalid username.')

        if len(username) > 16:
            raise HttpBadRequestError('Username to long.')

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not re.match("^[a-zA-Z ]+$", name):
            raise HttpBadRequestError('Invalid name.')

        if len(name) > 32:
            raise HttpBadRequestError('Name to long.')

    async def __registry_user_info(self, user: User) -> User:
        return await self.__repository.register(user)

    @classmethod
    def __format_response(cls, user: User) -> Dict:
        count = len(user) if isinstance(user, list) else 1

        response = {
            "type": "User",
            "count": count,
            "attributes": {
                "id": str(user.id)
            }
        }

        return response
