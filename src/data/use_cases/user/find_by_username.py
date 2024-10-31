from typing import Dict
from src.domain.use_cases.user.find_by_username import IFindByUsername
from src.data.interfaces.user_repository import IUserRepository

class FindByUsername(IFindByUsername):
    def __init__(self, user_repository: IUserRepository):
        self.__user_repository = user_repository

    def find(self, username: str) -> Dict:
        pass
