from datetime import datetime
from src.infra.db.settings import Base
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, UUID, func

class Post_Comment(Base):
    __tablename__ = "post_comment"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    post_id: str = Column(UUID, ForeignKey("post.id"))
    author_id: str = Column(UUID, ForeignKey("user.id"))
    content: str = Column(String(1024), nullable=False)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at: datetime = Column(TIMESTAMP(timezone=True), default=None)
    deleted_at: datetime = Column(TIMESTAMP(timezone=True), default=None)