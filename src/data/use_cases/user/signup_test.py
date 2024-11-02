from src.infra.db.tests.user_repository import UserRepositorySpy
from src.infra.db.models.user import User
from .signup import Signup

def test_register():
    mocked_user = User(username = 'test_21', full_name = 'Test Sigma', password = 'testing123')

    repo = UserRepositorySpy()
    user_register = Signup(repo)

    response = user_register.register(mocked_user)

    assert repo.register_attributes.username == mocked_user.username
    assert repo.register_attributes.full_name == mocked_user.full_name
    assert repo.register_attributes.password == mocked_user.password

    assert response["type"] == "User"
    assert response["count"] == 1
    assert response["attributes"]

def test_register_invalid_name_error():
    mocked_user = User(username = 'test_21', full_name = 'Test Sigma_123', password = 'testing123')

    repo = UserRepositorySpy()
    user_register = Signup(repo)

    try:
        user_register.register(mocked_user)
        assert False

    except Exception as err:
        assert str(err) == "Invalid name."

def test_register_invalid_username():
    mocked_user = User(username = 'test 21', full_name = 'Test Sigma', password = 'testing123')

    repo = UserRepositorySpy()
    user_register = Signup(repo)

    try:
        user_register.register(mocked_user)
        assert False

    except Exception as err:
        assert str(err) == "Invalid username."

def test_register_to_long_username():
    mocked_user = User(username = 'test_24_7_every_day_every_mount', full_name = 'Test Sigma', password = 'testing123')

    repo = UserRepositorySpy()
    user_register = Signup(repo)

    try:
        user_register.register(mocked_user)
        assert False

    except Exception as err:
        assert str(err) == "Username to long."
