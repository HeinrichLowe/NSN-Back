from abc import ABC, abstractmethod
from typing import Dict

class IGetBasicUserInfo(ABC):
    @abstractmethod
    async def execute(self, user_id: str) -> Dict:
        pass
