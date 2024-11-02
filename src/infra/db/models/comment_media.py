from datetime import datetime
from sqlalchemy import Column, ForeignKey, TIMESTAMP, UUID, func
from sqlalchemy.orm import relationship
from src.infra.db.settings import Base

class CommentMedia(Base):
    __tablename__ = "comment_media"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    comment_id: str = Column(UUID, ForeignKey("comment.id"), unique=True)
    media_id: str = Column(UUID, ForeignKey("media.id"))
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable

    # Relationship
    comment = relationship("Comment", back_populates="media")
    media = relationship("Media")
