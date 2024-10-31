from src.infra.db.repositories import UserRepository
from src.data.use_cases.user.user_register import UserRegister
from src.data.use_cases.user.token_generator import TokenGenerator
from src.presentation.controllers.users.register import RegisterController

def register_composer():
    repository = UserRepository()
    token_generator = TokenGenerator()
    use_case = UserRegister(repository, token_generator)
    controller = RegisterController(use_case)

    return controller
