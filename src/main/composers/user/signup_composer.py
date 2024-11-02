from src.infra.db.repositories import UserRepository
from src.data.use_cases.user.signup import Signup
from src.data.use_cases.user.token_generator import TokenGenerator
from src.presentation.controllers.users.signup import SignupController

def signup_composer():
    repository = UserRepository()
    token_generator = TokenGenerator()
    use_case = Signup(repository, token_generator)
    controller = SignupController(use_case)

    return controller
