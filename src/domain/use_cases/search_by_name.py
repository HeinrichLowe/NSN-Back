from abc import ABC, abstractmethod
from typing import List

class ISearchByName(ABC):
    @abstractmethod
    def find(self, name: str) -> List:
        pass
