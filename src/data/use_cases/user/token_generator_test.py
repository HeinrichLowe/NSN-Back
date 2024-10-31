from uuid import uuid4
import pytest
from src.domain.entities.user import User
from .token_generator import TokenGenerator


@pytest.mark.asyncio
async def test_create_tokens():
    token_generator = TokenGenerator()

    user_data = User({
        "id": uuid4(),
        "username": "test"
    })

    tokens = await token_generator.create_tokens(user_data)

    assert tokens is not None
    assert "access_token" in tokens
    assert "refresh_token" in tokens

@pytest.mark.asyncio
async def test_verify_access_token():
    token_generator = TokenGenerator()

    user_data = User({
        "id": uuid4(),
        "username": "test"
    })

    tokens = await token_generator.create_tokens(user_data)

    verified_token = await token_generator.verify_token(tokens["access_token"])

    assert verified_token is not None
    assert verified_token["sub"]["user_id"] == str(user_data.id)
