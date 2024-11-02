from enum import Enum
from datetime import datetime
from sqlalchemy import Column, String, Integer, TIMESTAMP, UUID, func, Enum as SQLEnum
from src.infra.db.settings import Base

class MediaType(str, Enum):
    IMAGE = "image"
    VIDEO = "video"

class Media(Base):
    __tablename__ = "media"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    content_type: str = Column(String(50), nullable=False)  # MIME type (image/jpeg, video/mp4, etc)
    media_type: MediaType = Column(SQLEnum(MediaType), nullable=False)
    url: str = Column(String, nullable=False)
    thumbnail_url: str = Column(String, nullable=True)
    width: int = Column(Integer, nullable=True)
    height: int = Column(Integer, nullable=True)
    duration: int = Column(Integer, nullable=True)  # para vídeos (em segundos)
    size: int = Column(Integer, nullable=False)  # tamanho em bytes
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable
