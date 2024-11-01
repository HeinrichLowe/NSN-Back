from abc import ABC, abstractmethod
from typing import Dict
from src.domain.entities.user import User

class ISignIn(ABC):
    @abstractmethod
    async def execute(self, credentials: User) -> Dict:
        pass
