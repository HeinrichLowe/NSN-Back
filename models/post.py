from db.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, UUID, func
from datetime import datetime

class Post(Base):
    __tablename__ = "post"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    author_id: str = Column(UUID, ForeignKey("user.id"))
    title: str = Column(String(128))
    content: str = Column(String(1024), nullable=False)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at: datetime = Column(TIMESTAMP(timezone=True), default=None)
    deleted_at: datetime = Column(TIMESTAMP(timezone=True), default=None)