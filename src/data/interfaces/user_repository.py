from typing import List
from abc import ABC, abstractmethod
from src.infra.db.models import User
from src.domain.entities.user import User as UserEntity

class IUserRepository(ABC):
    @abstractmethod
    async def get_all(self) -> List[UserEntity]:
        pass

    @abstractmethod
    async def register(self, user: User) -> UserEntity:
        pass

    """
    def update_inf(self, conn, user, params):
        pass

    async def search_by_id(self, db_session: AsyncSession, credentials: User) -> User:
        pass

    async def search_by_credentials(self, db_session: AsyncSession, credentials: User) -> User:
        pass
    """

    @abstractmethod
    async def search_by_username(self, username: str) -> UserEntity:
        pass

    """
    def my_profile(self, conn, user_id):
        pass
    """

    @abstractmethod
    async def search_by_name(self, name):
        pass

    """
    def add_friend(self, conn, user, friend):
        pass

    def input_date(self):
        pass

    def search_by_id_old(self, conn, user_logged):
        pass

    def search_by_friend_id(self, conn, friends_id):
        pass

    def delete_account(self, conn, user):
        pass

    def delete_friend(self, conn, user, friend):
        pass

    def friends_select(self, conn, user):
        pass

    def soft_delete_user(self, conn, user):
        pass

    def user_verify(self, conn, user_id):
        pass
        
    def edit_email(conn, cookie):
        pass

    def edit_username(conn, cookie):
        pass

    def edit_password(conn, cookie):
        pass

    def edit_realname(conn, cookie):
        pass

    def edit_birthday(conn, cookie):
        pass
    """
