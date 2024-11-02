from datetime import datetime
from sqlalchemy import Column, ForeignKey, TIMESTAMP, UUID, func, String
from sqlalchemy.orm import relationship
from src.infra.db.settings import Base

class PostShare(Base):
    __tablename__ = "post_share"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    user_id: str = Column(UUID, ForeignKey("user.id"), nullable=False)
    post_id: str = Column(UUID, ForeignKey("post.id"), nullable=False)
    comment: str = Column(String(280), nullable=True)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable
    deleted_at: datetime = Column(TIMESTAMP(timezone=True), default=None)

    # Relationships
    user = relationship("User", back_populates="shared_posts")
    post = relationship("Post", back_populates="shares")
