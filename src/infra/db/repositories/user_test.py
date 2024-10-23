import pytest
from sqlalchemy import insert, select, delete
from src.infra.db.settings.connection import Connection
from src.infra.db.models.user import User
from .user import UserRepository

@pytest.mark.skip(reason="Database dependent testing")
@pytest.mark.asyncio
async def test_register():
    mocked_user = User(username = 'test_18', full_name = 'Test_Teta', password = 'testing123')

    user_repository = UserRepository()
    await user_repository.register(mocked_user)

    sql = select(User).where(
        User.username == mocked_user.username,
        User.full_name == mocked_user.full_name
    )

    async with Connection() as session:
        result = await session.execute(sql)
        response = result.scalar_one_or_none()
        await session.execute(delete(User).where(User.id==response.id))
        await session.commit()

    assert response.username == mocked_user.username
    assert response.full_name == mocked_user.full_name
    assert response.password == mocked_user.password

@pytest.mark.skip(reason="Database dependent testing")
@pytest.mark.asyncio
async def test_search_by_username():
    mocked_user = User(username = 'test_19', full_name = 'Test_Teta', password = 'testing123')

    async with Connection() as session:
        await session.execute(insert(User).values(username=mocked_user.username, full_name=mocked_user.full_name, password=mocked_user.password))
        await session.commit()

        user_repository = UserRepository()
        response = await user_repository.search_by_username(mocked_user.username)

        await session.execute(delete(User).where(User.id==response.id))
        await session.commit()

    assert response.username == mocked_user.username
    assert response.full_name == mocked_user.full_name
    assert response.password == mocked_user.password
