from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from fastapi import Depends
from decouple import config

DB_URL = config('DB_URL')

def connect_db():
    engine = create_async_engine(DB_URL, pool_pre_ping=True, echo=True)
    return async_sessionmaker(engine, expire_on_commit=False)

class Connection:
    @classmethod
    def db_session(cls):
        if not hasattr(cls, '_db_connection'):
            cls._db_connection = connect_db()
        return cls._db_connection

DependsConnection: async_sessionmaker = Depends(Connection.db_session)