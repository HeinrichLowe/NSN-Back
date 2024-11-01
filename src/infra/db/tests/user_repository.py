from typing import List
from src.infra.db.models.user import User
from src.domain.entities.user import User as UserEntity

class UserRepositorySpy:
    def __init__(self):
        self.get_all_attributes = {}
        self.register_attributes = {}
        self.search_by_username_attributes = {}
        self.search_by_name_attributes = {}
        self.signin_attributes = {}

    def get_all(self) -> List[UserEntity]:
        pass

    def register(self, user: User) -> UserEntity:
        response = self.register_attributes = user
        return response

    def search_by_username(self, username) -> UserEntity:
        self.search_by_username_attributes["username"] = username
        return self.search_by_username_attributes

    def search_by_name(self, name: str) -> List[UserEntity]:
        self.search_by_name_attributes["name"] = name
        return [
            User(username = 'test_97', full_name = 'Test_Terayotabite', password = 'testing123'),
            User(username = 'test_98', full_name = 'Test_Pentayotabite', password = 'testing123'),
            User(username = 'test_99', full_name = 'Test_Hexayotabite', password = 'testing123')
        ]
    
    def signin(self, name: str) -> List[UserEntity]:
        self.search_by_name_attributes["name"] = name
        return [
            User(username = 'test_97', full_name = 'Test_Terayotabite', password = 'testing123'),
            User(username = 'test_98', full_name = 'Test_Pentayotabite', password = 'testing123'),
            User(username = 'test_99', full_name = 'Test_Hexayotabite', password = 'testing123')
        ]
