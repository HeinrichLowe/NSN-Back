from typing import Dict
from src.domain.entities.user import User

class RegisterSpy:
    def __init__(self):
        self.search_attribute = None

    def register(self, user: User) -> Dict:
        self.search_attribute = user

        count = len(user) if isinstance(user, list) else 1

        return {
            "type": "User",
            "count": count,
            "attributes": vars(self.search_attribute)
        }
