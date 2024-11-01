from abc import ABC, abstractmethod

class IHashComparer(ABC):
    @abstractmethod
    def compare(self, income_password: str, stored_password: str) -> bool:
        """Compares a plaintext with a hash"""
