from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.infra.db.settings.database_url import get_database_url

class Connection:
    def __init__(self):
        self.__connection_string = get_database_url()
        self._db_connection = None
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_async_engine(self.__connection_string, pool_pre_ping=True, echo=True)
        return engine

    def get_engine(self):
        return self.__engine

    async def __aenter__(self):
        session_make = async_sessionmaker(self.__engine, expire_on_commit=False)
        self.session = session_make()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
