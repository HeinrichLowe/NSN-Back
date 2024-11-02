from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, UniqueConstraint, UUID, func, TIMESTAMP, CheckConstraint
from src.infra.db.settings import Base

class Like(Base):
    __tablename__ = "like"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    user_id: str = Column(UUID, ForeignKey("user.id"), nullable=False)
    content_id: str = Column(UUID, nullable=False)  # Post or Comment ID
    content_type: str = Column(String(10), nullable=False)  # "post" or "comment"
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable

    __table_args__ = (
        UniqueConstraint('user_id', 'content_id', 'content_type', name='uq_user_content_like'),
        CheckConstraint(
            "content_type IN ('post', 'comment')",
            name='check_content_type'
        )
    )
