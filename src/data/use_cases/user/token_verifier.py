from typing import Dict
import jwt
from decouple import config
from src.domain.use_cases.user.token_verifier import ITokenVerifier
from src.errors.types import HttpUnauthorizedError

class TokenVerifier(ITokenVerifier):
    def __init__(self):
        self.__secret_key = config('SECRET_KEY')
        self.__algorithm = config('ALGORITHM')

    async def verify_token(self, token: str) -> Dict:
        try:
            payload = jwt.decode(token, self.__secret_key, algorithms=[self.__algorithm])
            return payload

        except jwt.ExpiredSignatureError as err:
            raise HttpUnauthorizedError("Token expirado") from err
        except jwt.InvalidTokenError as err:
            raise HttpUnauthorizedError("Token inválido") from err
        except Exception as err:
            raise HttpUnauthorizedError(f"Erro na verificação do token: {str(err)}") from err
