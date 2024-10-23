from typing import Dict
from src.domain.use_cases.find_by_username import IFindByUsername
from src.data.interfaces.user_repository import IUserRepository

class FindByUsername(IFindByUsername):
    def __init__(self, users_repository: IUserRepository):
        self.__users_repository = users_repository

    def find(self, username: str) -> Dict:
        pass
