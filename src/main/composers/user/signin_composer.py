from src.infra.db.repositories import UserRepository
from src.data.use_cases.user.signin import Signin
from src.data.use_cases.user.token_generator import TokenGenerator
from src.presentation.controllers.users.signin import SigninController
from src.infra.cryptography.hash_handler import PasslibHashHandler

def signin_composer():
    repository = UserRepository()
    token_generator = TokenGenerator()
    hash_comparer = PasslibHashHandler()
    use_case = Signin(repository, token_generator, hash_comparer)
    controller = SigninController(use_case)

    return controller
