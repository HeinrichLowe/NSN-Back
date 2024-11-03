from typing import Dict
from src.domain.use_cases.user.get_basic_user_info import IGetBasicUserInfo
from src.data.interfaces.user_repository import IUserRepository
from src.domain.entities.user import User as UserEntity
from src.errors.types import HttpBadRequestError

class GetBasicUserInfo(IGetBasicUserInfo):
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository = user_repository

    async def execute(self, user_id: str) -> Dict:
        user = await self.__find_user(user_id)
        return self.__format_response(user)

    async def __find_user(self, user_id: str) -> UserEntity:
        user = await self.__user_repository.find_by_id(user_id)
        if not user:
            raise HttpBadRequestError("User not found")
        return user

    @classmethod
    def __format_response(cls, user: UserEntity) -> Dict:
        count = len(user) if isinstance(user, list) else 1

        attributes = {
            "full_name": user.full_name,
            "avatar": user.avatar,
        }

        response = {
            "type": "User",
            "count": count,
            "attributes": attributes
        }

        return response
