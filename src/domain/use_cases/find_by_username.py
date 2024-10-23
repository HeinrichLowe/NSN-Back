from abc import ABC, abstractmethod
from typing import Dict

class IFindByUsername(ABC):
    @abstractmethod
    def find(self, username: str) -> Dict:
        pass
