import datetime
#from repositories.user import UserCommand
#from models.migrations import User
from passlib.hash import pbkdf2_sha256
import jwt
from decouple import config

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')
ACCESS_TOKEN_EXPIRATION = config('ACCESS_TOKEN_EXPIRATION')
REFRESH_TOKEN_EXPIRATION = config('REFRESH_TOKEN_EXPIRATION')
Sha = pbkdf2_sha256

async def signup(db_session, input):
    if not input.email and not input.username:
        raise {'status_code': 400, 'detail': "Email or username must be provided."}

    user_on_db = await UserCommand.register(db_session, User(
        email=input.email,
        username=input.username.lower() if input.username else None,
        password=Sha.hash(input.password),
        full_name=input.full_name,
        birthday=input.birthday

    ))
    
    access_exp = datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=int(ACCESS_TOKEN_EXPIRATION))

    payload = {
        'sub': {
            "username": input.username,
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