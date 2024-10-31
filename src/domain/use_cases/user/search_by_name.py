from abc import ABC, abstractmethod
from typing import List

class ISearchByName(ABC):
    @abstractmethod
    async def find(self, name: str) -> List:
        pass
