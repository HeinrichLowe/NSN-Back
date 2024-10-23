from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from fastapi import Depends
from decouple import config

DB_DIALECT_DRIVER = config('DB_DIALECT_DRIVER')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')

class Connection:
    def __init__(self):
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(        # pylint: disable=consider-using-f-string
            DB_DIALECT_DRIVER,
            DB_USER,
            DB_PASSWORD,
            DB_HOST,
            DB_PORT,
            DB_NAME
        )
        self._db_connection = None
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_async_engine(self.__connection_string, pool_pre_ping=True, echo=True)
        return engine

    def get_engine(self):
        return self.__engine

    def db_session(self): # Revisar a necessidade
        if not hasattr(self, '_db_connection'):
            self._db_connection = self.__create_database_engine()
        return self._db_connection

    async def __aenter__(self):
        session_make = async_sessionmaker(self.__engine, expire_on_commit=False)
        self.session = session_make()
        return self.session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

DependsConnection: async_sessionmaker = Depends(Connection.db_session) # Revisar a necessidade
# Se necessário, comparar o uso com a versão que está no GitHub.
