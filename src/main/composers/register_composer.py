from src.infra.db.repositories import UserRepository
from src.data.use_cases.user_register import UserRegister
from src.presentation.controllers.users.register import RegisterController

def register_composer():
    repository = UserRepository()
    use_case = UserRegister(repository)
    controller = RegisterController(use_case)

    return controller.handle
