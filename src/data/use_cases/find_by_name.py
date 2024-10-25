from typing import List, Dict
import re
from src.domain.use_cases.find_by_name import IFindByName
from src.data.interfaces.user_repository import IUserRepository
from src.domain.entities.user import User

class FindByName(IFindByName):
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository = user_repository

    def find(self, name: str) -> List:
        self.__validate_name(name)
        users = self.__search_user(name)
        return self.__format_response(users)

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not re.match("^[a-zA-Z ]+$", name):
            raise Exception('Invalid name.')

        if len(name) > 32:
            raise Exception('Name to long.')

    def __search_user(self, name: str) -> List[User]:
        users = self.__user_repository.search_by_name(name)
        if users == []:
            raise Exception('User not found.')
        return users

    @classmethod
    def __format_response(cls, users: List[User]) -> Dict:
        response = {
            "type": "User",
            "count": len(users),
            "attributes": users
        }

        return response
