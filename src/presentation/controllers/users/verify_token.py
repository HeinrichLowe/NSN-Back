from src.presentation.http_types import HttpRequest, HttpResponse
from src.presentation.interfaces.controller_interface import IController
from src.domain.use_cases.user.token_verifier import ITokenVerifier
from src.errors.types import HttpUnauthorizedError

class VerifyTokenController(IController):
    def __init__(self, token_verifier: ITokenVerifier):
        self.__token_verifier = token_verifier

    async def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.headers.get("Authorization")

        if not token:
            raise HttpUnauthorizedError("Token não fornecido")

        token = token.replace("Bearer ", "")

        payload = await self.__token_verifier.verify_token(token)

        return HttpResponse(
            status_code=200,
            body=payload
        )
