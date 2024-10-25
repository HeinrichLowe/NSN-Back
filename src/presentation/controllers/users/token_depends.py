from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
#from repositories import UserCommand
#from models.migrations import User
import jwt
from decouple import config
#from db.connect import DependsConnection as db_session

SECRET_KEY = config('SECRET_KEY')
ALGORITHM = config('ALGORITHM')

async def verify_token(access_token): # Token verify function
    data = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])

    await UserCommand.search_by_username(db_session, User(
        username=data['sub']
    ))

oauth_schema = OAuth2PasswordBearer

def token_depends(token = Depends(oauth_schema)): # Dependece to "middleware"
    verify_token(access_token=token)