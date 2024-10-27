from typing import List, Dict
import re
import uuid
from src.domain.use_cases.search_by_name import ISearchByName
from src.data.interfaces.user_repository import IUserRepository
from src.domain.entities.user import User

class SearchByName(ISearchByName):
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository = user_repository

    async def find(self, name: str) -> List:
        self.__validate_name(name)
        users = await self.__search_user(name)
        return self.__format_response(users)

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not re.match("^[a-zA-Z ]+$", name):
            raise Exception('Invalid name.')

        if len(name) > 32:
            raise Exception('Name to long.')

    async def __search_user(self, name: str) -> List[User]:
        users = await self.__user_repository.search_by_name(name)
        if users == []:
            raise Exception('User not found.')
        return users

    @classmethod
    def __format_response(cls, users: List[User]) -> Dict:
        count = len(users) if isinstance(users, list) else 1

        attributes = [{
            "id": str(user.id),
            "email": user.email,
            "full_name": user.full_name,
            "avatar": user.avatar,
        } for user in users]

        response = {
            "type": "User",
            "count": count,
            "attributes": attributes
        }

        return response
