import pytest
from src.infra.db.tests.user_repository import UserRepositorySpy
from src.infra.db.models.user import User
from .signin import Signin
from .token_generator import TokenGenerator

@pytest.mark.skip(reason="Test not implemented")
def test_register():
    pass
