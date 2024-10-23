from repositories.user import UserCommand
from models.migrations import User
from passlib.hash import pbkdf2_sha256
from decouple import config
import datetime
import jwt

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRATION = config('ACCESS_TOKEN_EXPIRATION')
REFRESH_TOKEN_EXPIRATION = config('REFRESH_TOKEN_EXPIRATION')
Sha = pbkdf2_sha256

async def refresh_token(db_session, input):
    print(input)
    user_on_db = await UserCommand.search_by_id(db_session, User(
        id=input
    ))

    access_exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=int(ACCESS_TOKEN_EXPIRATION))

    payload = {
        'sub': {
            "username": user_on_db.username,
            "user_id": user_on_db.id.hex
        },
        'exp': access_exp
    }

    access_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    refresh_exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=int(REFRESH_TOKEN_EXPIRATION))

    payload = {
        'sub': {
            "user_id": user_on_db.id.hex
        },
        'exp': refresh_exp
    }

    refresh_token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    return {
        'access_token': access_token,
        'access_exp': access_exp.isoformat(),
        'refresh_token': refresh_token,
        'refresh_exp': refresh_exp.isoformat()
    }