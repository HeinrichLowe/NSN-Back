from datetime import date
from sqlalchemy import TIMESTAMP, UUID

class User:
    def __init__(
            self,
            id: UUID, # pylint: disable=redefined-builtin
            email: str,
            username: str,
            password: str,
            full_name: str,
            avatar: str,
            birthday: date,
            created_at: TIMESTAMP,
            deleted_at: TIMESTAMP
        ) -> None:
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.full_name = full_name
        self.avatar = avatar
        self.birthday = birthday
        self.created_at = created_at
        self.deleted_at = deleted_at
