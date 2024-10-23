from src.infra.db.settings import Base
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, UUID, func

class Friend(Base):
    __tablename__ = "friend"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    user_id: str = Column(UUID, ForeignKey("user.id"))
    friend_id: str = Column(UUID, ForeignKey("user.id"))

    UniqueConstraint(user_id, friend_id)