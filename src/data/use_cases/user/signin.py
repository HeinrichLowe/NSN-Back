from typing import Dict
from src.domain.entities.user import User
from src.domain.use_cases.user.signin import ISignIn
from src.domain.use_cases.user.token_generator import ITokenGenerator
from src.domain.protocols.cryptography import IHashComparer
from src.infra.db.repositories.user import UserRepository
from src.errors.types import HttpBadRequestError, HttpUnauthorizedError

class Signin(ISignIn):
    def __init__(self, user_repository: UserRepository, token_generator: ITokenGenerator, hash_comparer: IHashComparer):
        self.user_repository = user_repository
        self.__token_generator = token_generator
        self.__hash_comparer = hash_comparer

    async def execute(self, credentials: User) -> Dict:
        await self.__verify_username_or_email(credentials)
        await self.__verify_password(credentials)

        user = await self.__search_user(credentials)

        self.__hash_password_verify(credentials.password, user.password)
        tokens = await self.__token_generator.create_tokens(user)
        return self.__format_response(tokens)

    @classmethod
    async def __verify_username_or_email(cls, credentials: User) -> None:
        if not credentials.username and not credentials.email:
            raise HttpBadRequestError("Username or Email is required")

    @classmethod
    async def __verify_password(cls, credentials: User) -> None:
        if not credentials.password:
            raise HttpBadRequestError("Password is required")

    async def __search_user(self, credentials: User) -> User:
        if credentials.username:
            user = await self.user_repository.search_by_username(credentials)
            if not user:
                raise HttpUnauthorizedError("Invalid credentials")
            return user
        if credentials.email:
            user = await self.user_repository.search_by_email(credentials)
            if not user:
                raise HttpUnauthorizedError("Invalid credentials")
            return user

    def __hash_password_verify(self, income_password: str, stored_password: str) -> None:
        if not self.__hash_comparer.compare(income_password, stored_password):
            raise HttpUnauthorizedError("Invalid credentials")

    @classmethod
    def __format_response(cls, tokens: Dict) -> Dict:
        count = len(tokens) if isinstance(tokens, list) else 1

        response = {
            "type": "User",
            "count": count,
            "attributes": {
                **tokens
            }
        }

        return response
