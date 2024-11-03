from src.data.use_cases.user.token_verifier import TokenVerifier
from src.presentation.controllers.users.verify_token import VerifyTokenController

def verify_token_composer():
    token_verifier = TokenVerifier()
    controller = VerifyTokenController(token_verifier)

    return controller
