from datetime import datetime
from sqlalchemy import Column, String, TIMESTAMP, UUID, func, CheckConstraint
from src.infra.db.settings import Base

class HashTag(Base):
    __tablename__ = "hashtag"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    name: str = Column(String(140), nullable=False, unique=True)  # Unique to prevent duplicates
    created_at: datetime = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable

    __table_args__ = (
        # Grant that the hashtag name starts with #
        CheckConstraint("name LIKE '#%'", name='check_hashtag_format'),
    )
