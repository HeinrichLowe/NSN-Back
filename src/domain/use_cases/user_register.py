from abc import ABC, abstractmethod
from typing import Dict
from src.domain.entities.user import User

class IUserRegister(ABC):
    @abstractmethod
    def register(self, user: User) -> Dict:
        pass
