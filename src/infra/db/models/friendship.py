from datetime import datetime
from enum import Enum
from sqlalchemy import Column, String, TIMESTAMP, UUID, ForeignKey, UniqueConstraint, CheckConstraint, func
from src.infra.db.settings import Base

class FriendshipStatus(str, Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class Friendship(Base):
    __tablename__ = "friendship"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    requester_id: str = Column(UUID, ForeignKey("user.id"), nullable=False)
    addressee_id: str = Column(UUID, ForeignKey("user.id"), nullable=False)
    status: str = Column(String(10), nullable=False, default=FriendshipStatus.PENDING.value)
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable
    updated_at: datetime = Column(TIMESTAMP(timezone=True), onupdate=func.now()) # pylint: disable=not-callable

    __table_args__ = (
        # Prevent duplicate friendships
        UniqueConstraint('requester_id', 'addressee_id', name='uq_friendship'),
        # Prevent user from being friend with himself
        CheckConstraint('requester_id != addressee_id', name='check_self_friendship'),
        # Grant valid status
        CheckConstraint(
            f"status IN {tuple(status.value for status in FriendshipStatus)}",
            name='check_friendship_status'
        )
    )
