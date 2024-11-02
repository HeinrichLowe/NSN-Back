from sqlalchemy import Column, String, Boolean, Date, TIMESTAMP, Index, UUID, func
from sqlalchemy.orm import relationship
from src.infra.db.settings import Base

class User(Base):
    __tablename__ = "user"

    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    email = Column(String, nullable=True)
    username = Column(String(64), nullable=True)
    password = Column(String(256), nullable=False)
    full_name = Column(String(512), nullable=False)
    phone_number = Column(String(16), nullable=True)
    bio = Column(String(1024), nullable=True)
    avatar = Column(String)
    birth_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now()) # pylint: disable=not-callable
    deleted_at = Column(TIMESTAMP(timezone=True), server_default=None)
    is_active = Column(Boolean, default=False)

    Index('uni_username', username, unique=True, postgresql_where=deleted_at is None)
    Index('uni_user_email', email, unique=True, postgresql_where=deleted_at is None)

    shared_posts = relationship("PostShare", back_populates="user")

    def __repr__(self):
        return f"<User(username='{self.username}', full_name='{self.full_name}', email='{self.email}')>"
