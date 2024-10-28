from datetime import datetime
from typing import List
from sqlalchemy import insert, select#, update, delete, func
from src.infra.db.settings.connection import Connection
from src.infra.db.models.user import User
from src.domain.entities.user import User as UserEntity
from src.data.interfaces.user_repository import IUserRepository

class UserRepository(IUserRepository):
    async def get_all(self) -> List[UserEntity]:
        async with Connection() as session:
            result =  await session.execute(select(User))
            return result.all()

    async def register(self, user: User) -> UserEntity:
        async with Connection() as session:
            try:
                sql = insert(User).\
                    values(
                        email=user.email,
                        username=user.username,
                        password=user.password,
                        full_name=user.full_name,
                        birthday=user.birthday
                ).\
                    returning(User)

                result = await session.execute(sql)
                await session.commit()
                return result.scalar_one_or_none()

            except Exception as err:
                await session.rollback()
                raise err
    """
    def update_inf(self, conn, user, params):
        with conn.begin() as cur:
            try:
                sql = update(User) \
                .where(User.id == user.id) \
                .values(params)
                cur.execute(sql)
            except Exception as err:
                print(err)
                raise Exception()

    async def search_by_id(self, db_session: AsyncSession, credentials: User) -> User:
        async with db_session() as conn:
            sql = select(User).where(
                User.id == credentials.id,
                User.deleted_at is None
            )
            result = await conn.execute(sql)
            return result.scalars().one()

    async def search_by_credentials(self, db_session: AsyncSession, credentials: User) -> User:
        async with db_session() as conn:
            sql = select(User).where(
                User.username == credentials.username,
                User.password == credentials.password,
                User.deleted_at is None
            )
            result = await conn.execute(sql)
            return result.scalars().one()
    """

    async def search_by_username(self, username: str) -> UserEntity:
        async with Connection() as session:
            try:
                sql = select(User).where(User.username == username, User.deleted_at.is_(None))
                result = await session.execute(sql)
                return result.scalars().first()

            except Exception as err:
                await session.rollback()
                raise err

# Refactory ↓↓↓
    """
    def my_profile(self, conn, user_id):
        with conn.connect() as cur:
            try:
                profile = cur.execute(select(User).where(User.id == user_id)).all()
                #profile.friends = cur.execute(select(Friends).where(Friends.id == user_id)).scallar()
                #profile['birthday'].strftime("%d/%m/%Y")
                if not profile:
                    raise Exception
                return profile
            except Exception as err:
                print(err)
    """

    async def search_by_name(self, name: str) -> List[UserEntity]:
        async with Connection() as session:
            try:
                sql = await session.execute(select(User).where(User.full_name.ilike(f"%{name}%")).order_by(User.id.desc()))
                response = sql.scalars().all()
                return response

            except Exception as err:
                print(err)
                raise err

    """
    def add_friend(self, conn, user, friend):
        with conn.begin() as cur:
            try:
                invert = {"user_id" : f"{friend['friend_id']}", "friend_id" : f"{user['user_id']}"}
                sql1 = insert(Friend).values(user | friend)
                sql2 = insert(Friend).values(invert)
                cur.execute(sql1)
                cur.execute(sql2)
            except Exception as err:
                print(err)
                raise Exception()

    def input_date(self):
        while True:
            try:
                bday = input("Enter your birthday (Ex: 15/06/2020): ")
                birthday = datetime.strptime(bday, "%d/%m/%Y")
                return birthday
            except:
                print("Invalid date, please, try again!")

    def search_by_id_old(self, conn, user_logged):
        with conn.connect() as cur:
            try:
                sql = select(User).where(User.id==user_logged)
                print(type(user_logged))
                return cur.execute(sql).one()
            except Exception as err:
                print(err)
                raise Exception()

    def search_by_friend_id(self, conn, friends_id):
        with conn.connect() as cur:
            try:
                sql = select(User).where(User.id==friends_id.user_id)
                print(type(friends_id))
                return cur.execute(sql).all()
            except Exception as err:
                print(err)
                raise Exception()

    def delete_account(self, conn, user):
        with conn.begin() as cur:
            try:
                sql = delete(User).where(User.id==user.id)
                return cur.execute(sql)
            except Exception as err:
                print(err)

    def delete_friend(self, conn, user, friend):
        with conn.begin() as cur:
            try:
                sql1 = delete(Friend).where(Friend.user_id==user.id, Friend.friend_id==friend.id)
                sql2 = delete(Friend).where(Friend.friend_id==user.id, Friend.user_id==friend.id)
                cur.execute(sql1)
                cur.execute(sql2)
            except Exception as err:
                print(err)

    def friends_select(self, conn, user):
        with conn.connect() as cur:
            try:
                sql = select(User).where(User.id==Friend.friend_id, Friend.friend_id!=user.id)
                return cur.execute(sql).all()
            except Exception as err:
                print(err)

    def soft_delete_user(self, conn, user):
        with conn.begin() as cur:
            try:
                sql = update(User).values(deleted_at=func.now()).where(User.id==user.id)
                cur.execute(sql)
            except Exception:
                raise Exception()

    def user_verify(self, conn, user_id):
        with conn.begin() as cur:
            user = cur.execute(select(User).where(User.id == user_id, User.deleted_at == None)).fetchone()
            if not user:
                raise Exception()
            return user
"""
"""
    def edit_email(conn, cookie):
        with conn.connect() as cur:
            temp=input("Enter your new email: ")
            try:
                verify = cur.execute(select(Users.id).where(Users.email == temp)).all()
                if not verify:
                    sql = update(Users).where(Users.email == cookie['user'].email).values(email=temp)
                    cur.execute(sql)
                    cur.commit()
                else:
                    print("\nThis email is already in use. Please try another email!")
            except Exception as err:
                print(f"Error: {err}")

    def edit_username(conn, cookie):
        with conn.connect() as cur:
            temp=input("Enter your new username: ")
            try:
                verify = cur.execute(select(Users.id).where(Users.username == temp)).all()
                if not verify:
                    sql = update(Users).where(Users.username == cookie['user'].username).values(username=temp)
                    cur.execute(sql)
                    cur.commit()
                else:
                    print("\nThis username is already in use. Please try another username!")
            except Exception as err:
                print(f"Error: {err}")

    def edit_password(conn, cookie):
        with conn.connect() as cur:
            temp=input("Enter your new password: ")
            try:
                old_password = input("Enter your old password: ")
                verify_old_password = cur.execute(select(Users.password).where(Users.id == cookie['user'].id)).one()
                if old_password in verify_old_password:
                    sql = update(Users).where(Users.password == cookie['user'].password).values(password=temp)
                    cur.execute(sql)
                    cur.commit()
                else:
                    print("\nOops, something is go wrong, please, try again!")
            except Exception as err:
                print(f"Error: {err}")

    def edit_realname(conn, cookie):
        with conn.connect() as cur:
            temp=input("Enter your name: ")
            try:
                sql = update(Users).where(Users.full_name == cookie['user'].full_name).values(full_name=temp)
                cur.execute(sql)
                cur.commit()
            except Exception as err:
                print(f"Error: {err}")

    def edit_birthday(conn, cookie):
        with conn.connect() as cur:
            temp=input("Enter your birthday (Ex: 15/06/2020): ")
            bday = datetime.strptime(temp, "%d/%m/%Y")
            try:
                sql = update(Users).where(Users.birthday == cookie['user'].birthday).values(birthday=bday)
                cur.execute(sql)
                cur.commit()
            except Exception as err:
                print(f"Error: {err}")
"""