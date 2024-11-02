from datetime import datetime
from sqlalchemy import Column, String, TIMESTAMP, UUID, ForeignKey, Boolean, CheckConstraint, func
from src.infra.db.settings import Base

class Message(Base):
    __tablename__ = "message"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    sender_id: str = Column(UUID, ForeignKey("user.id"), nullable=False)
    receiver_id: str = Column(UUID, ForeignKey("user.id"), nullable=False)
    content: str = Column(String(1024), nullable=False)
    is_read: bool = Column(Boolean, default=False)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable
    deleted_at: datetime = Column(TIMESTAMP(timezone=True), nullable=True)  # soft delete

    __table_args__ = (
        # Prevent messages to oneself
        CheckConstraint('sender_id != receiver_id', name='check_self_message'),
    )
