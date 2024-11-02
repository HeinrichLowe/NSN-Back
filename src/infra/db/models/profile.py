from sqlalchemy import Column, String, ForeignKey, UUID, func
from src.infra.db.settings import Base

class Profile(Base): # pylint: disable=inherit-non-class
    ''' Profile table representation '''

    __tablename__ = "profile"

    id = Column(UUID, primary_key=True, server_default=func.uuid_generate_v4())
    user_id = Column(UUID, ForeignKey('user.id'))
    location = Column(String(1024), nullable=True)
    website = Column(String(1024), nullable=True)
    background_image = Column(String, nullable=True)
