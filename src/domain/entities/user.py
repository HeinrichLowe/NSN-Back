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
            avatar: str = None,
            birthday: date = None,
            created_at: TIMESTAMP = None,
            deleted_at: TIMESTAMP = None
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
