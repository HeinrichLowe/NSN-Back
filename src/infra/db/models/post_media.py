from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, UUID, CheckConstraint, UniqueConstraint, func
from sqlalchemy.orm import relationship
from src.infra.db.settings import Base

class PostMedia(Base):
    __tablename__ = "post_media"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    post_id: str = Column(UUID, ForeignKey("post.id"))
    media_id: str = Column(UUID, ForeignKey("media.id"))
    position: int = Column(Integer, nullable=False)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable

    # Relationship
    post = relationship("Post", back_populates="media")
    media = relationship("Media")

    __table_args__ = (
        # Garante máximo 4 mídias por post
        CheckConstraint('position >= 0 AND position < 4', name='check_position_range'),
        # Garante que cada posição é única por post
        UniqueConstraint('post_id', 'position', name='uq_post_media_position')
    )
