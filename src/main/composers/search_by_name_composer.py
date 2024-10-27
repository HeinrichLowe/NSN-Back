from src.infra.db.repositories import UserRepository
from src.data.use_cases.search_by_name import SearchByName
from src.presentation.controllers.users.search_by_name import SearchByNameController

def search_by_name_composer():
    repository = UserRepository()
    use_case = SearchByName(repository)
    controller = SearchByNameController(use_case)

    return controller
