from datetime import datetime
from sqlalchemy import Column, ForeignKey, TIMESTAMP, UUID, func, UniqueConstraint
from sqlalchemy.orm import relationship
from src.infra.db.settings import Base

class PostHashTag(Base):
    __tablename__ = "post_hashtag"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    post_id: str = Column(UUID, ForeignKey("post.id"), nullable=False)
    hashtag_id: str = Column(UUID, ForeignKey("hashtag.id"), nullable=False)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable

    # Relationships
    post = relationship("Post", back_populates="hashtags")
    hashtag = relationship("HashTag")

    __table_args__ = (
        # Prevent the same hashtag from being associated with the same post more than once
        UniqueConstraint('post_id', 'hashtag_id', name='uq_post_hashtag'),
    )
