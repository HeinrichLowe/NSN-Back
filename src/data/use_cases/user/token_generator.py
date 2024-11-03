from typing import Dict
import datetime
import jwt
from decouple import config
from src.domain.entities.user import User
from src.domain.use_cases.user.token_generator import ITokenGenerator

class TokenGenerator(ITokenGenerator):
    def __init__(self):
        self.__secret_key = config('SECRET_KEY')
        self.__algorithm = config('ALGORITHM')
        self.__access_token_expiration = config('ACCESS_TOKEN_EXPIRATION')
        self.__refresh_token_expiration = config('REFRESH_TOKEN_EXPIRATION')

    async def __generate_access_token(self, user_data: User) -> Dict:
        access_exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=int(self.__access_token_expiration))

        payload = {
            'sub': {
                "username": user_data.username,
                "user_id": str(user_data.id)
            },
            'exp': access_exp
        }

        access_token = jwt.encode(payload=payload, key=self.__secret_key, algorithm=self.__algorithm)

        return {
            'access_token': access_token,
            'access_exp': access_exp.isoformat()
        }

    async def __generate_refresh_token(self, user_data: User) -> Dict:
        refresh_exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=int(self.__refresh_token_expiration))

        payload = {
            'sub': {
                "user_id": str(user_data.id)
            },
            'exp': refresh_exp
        }

        refresh_token = jwt.encode(payload=payload, key=self.__secret_key, algorithm=self.__algorithm)

        return {
            'refresh_token': refresh_token,
            'refresh_exp': refresh_exp.isoformat()
        }

    async def create_tokens(self, user_data: User) -> Dict:
        access_token = await self.__generate_access_token(user_data)
        refresh_token = await self.__generate_refresh_token(user_data)

        return {
            **access_token,
            **refresh_token
        }
