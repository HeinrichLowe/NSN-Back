from datetime import date
from sqlalchemy import TIMESTAMP, UUID

class User:
    def __init__(
            self,
            id: UUID = None, # pylint: disable=redefined-builtin
            email: str = None,
            username: str = None,
            password: str = None,
            full_name: str = None,
            phone_number: str = None,
            bio: str = None,
            avatar: str = None,
            birth_date: date = None,
            created_at: TIMESTAMP = None,
            deleted_at: TIMESTAMP = None,
            is_active: bool = False
        ) -> None:
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.full_name = full_name
        self.phone_number = phone_number
        self.bio = bio
        self.avatar = avatar
        self.birth_date = birth_date
        self.created_at = created_at
        self.deleted_at = deleted_at
        self.is_active = is_active
