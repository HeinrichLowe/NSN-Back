from abc import ABC, abstractmethod
from typing import List

class IFindByName(ABC):
    @abstractmethod
    def find(self, name: str) -> List:
        pass
