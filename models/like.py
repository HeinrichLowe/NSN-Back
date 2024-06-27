from db.base import Base
from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint, UUID, func

class Like(Base):
    __tablename__ = "like"

    id: str = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    post_id: str = Column(UUID, ForeignKey("post.id"))
    author_id: str = Column(UUID, ForeignKey("user.id"))
    
    UniqueConstraint(post_id, author_id)