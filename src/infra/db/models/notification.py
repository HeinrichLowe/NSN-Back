from enum import Enum
from datetime import datetime
from sqlalchemy import Column, String, TIMESTAMP, UUID, ForeignKey, Boolean, CheckConstraint, func
from src.infra.db.settings import Base

class NotificationType(str, Enum):
    LIKE = "like"
    COMMENT = "comment"
    FOLLOW = "follow"
    MESSAGE = "message"

class Notification(Base):
    __tablename__ = "notification"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    user_id: str = Column(UUID, ForeignKey("user.id"), nullable=False)  # Who receives
    action_user_id: str = Column(UUID, ForeignKey("user.id"), nullable=False)  # Who caused the notification
    type: str = Column(String(20), nullable=False)
    content_id: str = Column(UUID, nullable=False)  # Related content ID
    content_type: str = Column(String(10), nullable=False)  # Content type
    is_read: bool = Column(Boolean, default=False)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable

    __table_args__ = (
        CheckConstraint(
            f"type IN {tuple(t.value for t in NotificationType)}",
            name='check_notification_type'
        ),
        CheckConstraint(
            "content_type IN ('post', 'comment', 'friendship', 'message')",
            name='check_content_type'
        )
    )
