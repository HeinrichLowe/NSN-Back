from db.base import Base
from sqlalchemy import Column, String, Date, TIMESTAMP, Index, UUID, func
from datetime import datetime

class User(Base):
    __tablename__ = "user"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    email: str = Column(String, nullable=False)
    username: str = Column(String(64), nullable=False)
    password: str = Column(String(256), nullable=False)
    full_name: str = Column(String(512), nullable=False)
    avatar: str = Column(String)
    birthday: str = Column(Date)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now())
    deleted_at: datetime = Column(TIMESTAMP(timezone=True), server_default=None)

    Index('uni_username', username, unique=True, postgresql_where=(deleted_at == None))
    Index('uni_user_email', email, unique=True, postgresql_where=(deleted_at == None))