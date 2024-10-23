from src.infra.db.settings import Base
from sqlalchemy import Column, Integer, ForeignKey, TIMESTAMP, UUID, func
from datetime import datetime

class Share(Base):
    __tablename__ = "share"
    
    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    author_id: str = Column(UUID, ForeignKey("user.id"))
    post_id: int = Column(Integer, nullable=False)
    deleted_at: datetime = Column(TIMESTAMP(timezone=True), default=None)