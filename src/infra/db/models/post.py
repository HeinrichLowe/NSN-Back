from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, UUID, func
from sqlalchemy.orm import relationship
from src.infra.db.settings import Base

class Post(Base):
    __tablename__ = "post"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    user_id: str = Column(UUID, ForeignKey("user.id"))
    title: str = Column(String(128))
    content: str = Column(String(1024), nullable=False)
    media = relationship("PostMedia", back_populates="post", cascade="all, delete-orphan")
    visibility: str = Column(String(16), nullable=False)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable
    updated_at: datetime = Column(TIMESTAMP(timezone=True), default=None)
    deleted_at: datetime = Column(TIMESTAMP(timezone=True), default=None)
    hashtags = relationship("PostHashTag", back_populates="post", cascade="all, delete-orphan")
    shares = relationship("PostShare", back_populates="post")
