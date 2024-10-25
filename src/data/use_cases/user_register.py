from typing import Dict
import re
from src.domain.use_cases.user_register import IUserRegister
from src.domain.entities.user import User
from src.data.interfaces.user_repository import IUserRepository

class UserRegister(IUserRegister):
    def __init__(self, repository: IUserRepository):
        self.__repository = repository

    def register(self, user: User) -> Dict:
        self.__validate_name(user.full_name)
        self.__validate_username(user.username)

        response = self.__registry_user_info(user)
        return self.__format_response(response)

    @classmethod
    def __validate_username(cls, username: str) -> None:
        if not re.match("^[a-zA-Z0-9_]+$", username):
            raise Exception('Invalid username.')

        if len(username) > 16:
            raise Exception('Username to long.')

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not re.match("^[a-zA-Z ]+$", name):
            raise Exception('Invalid name.')

        if len(name) > 32:
            raise Exception('Name to long.')

    def __registry_user_info(self, user: User) -> User:
        return self.__repository.register(user)

    @classmethod
    def __format_response(cls, user: User) -> Dict:
        count = len(user) if isinstance(user, list) else 1

        response = {
            "type": "User",
            "count": count,
            "attributes": user
        }

        return response
