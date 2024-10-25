from src.infra.db.tests.user_repository import UserRepositorySpy
from .find_by_name import FindByName

def test_find():
    name = "Brito Mada"

    repo = UserRepositorySpy()
    find_by_name = FindByName(repo)

    response = find_by_name.find(name)

    assert repo.search_by_name_attributes["name"] == name

    assert response["type"] == "User"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"] != []

def test_find_error_invalid_name():
    name = "Brito Mada 123"

    repo = UserRepositorySpy()
    find_by_name = FindByName(repo)

    try:
        find_by_name.find(name)
        assert False

    except Exception as err:
        assert str(err) == "Invalid name."

def test_find_error_too_long_name():
    name = "TestTestTestTestTestTestTestTestTest"

    repo = UserRepositorySpy()
    find_by_name = FindByName(repo)

    try:
        find_by_name.find(name)
        assert False

    except Exception as err:
        assert str(err) == "Name to long."

def test_find_error_user_not_found():
    class UserRepositoryError(UserRepositorySpy):
        def search_by_name(self, name: str):
            return []

    name = "Test"

    repo = UserRepositoryError()
    find_by_name = FindByName(repo)

    try:
        find_by_name.find(name)
        assert False

    except Exception as err:
        assert str(err) == "User not found."
