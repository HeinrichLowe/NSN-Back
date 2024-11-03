from src.infra.db.repositories.user import UserRepository
from src.data.use_cases.user.get_basic_user_info import GetBasicUserInfo
from src.presentation.controllers.users.get_basic_user_info import GetBasicUserInfoController

def get_basic_user_info_composer():
    repository = UserRepository()
    use_case = GetBasicUserInfo(repository)
    controller = GetBasicUserInfoController(use_case)

    return controller
