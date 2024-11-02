from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, UUID, func
from sqlalchemy.orm import relationship
from src.infra.db.settings import Base

class Comment(Base):
    __tablename__ = "comment"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    post_id: str = Column(UUID, ForeignKey("post.id"))
    user_id: str = Column(UUID, ForeignKey("user.id"))
    content: str = Column(String(1024), nullable=False)
    parent_id: str = Column(UUID, ForeignKey("comment.id"), nullable=True)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable
    deleted_at: datetime = Column(TIMESTAMP(timezone=True), default=None)

    # Relationship
    media = relationship("CommentMedia", back_populates="comment", uselist=False)  # max 1 midia
