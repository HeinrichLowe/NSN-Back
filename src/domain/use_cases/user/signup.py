from abc import ABC, abstractmethod
from typing import Dict
from src.domain.entities.user import User

class ISignup(ABC):
    @abstractmethod
    async def execute(self, user: User) -> Dict:
        pass
