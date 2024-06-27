from pydantic import BaseModel, Field, field_validator
from uuid import UUID
from datetime import datetime

class SignupRequest(BaseModel):
    email: str = Field(description="email do usuario")
    username: str = Field(min_length=3, max_length=32, description="nome do usuario para realizar o login")
    password: str = Field(min_length=6, max_length=64, description="password do usuario para realizar o login")
    full_name: str = Field(max_length=128, description="nome completo (ou não) do usário")
    birthday: str = Field(description="data de nascimento do usário. Ex: 01/01/1999")

    @field_validator("birthday")
    @classmethod
    def valid_bithday(cls, raw):
        date = datetime.strptime(raw, "%d/%m/%Y")
        return date

class SignupResponse(BaseModel):
    id: UUID = Field(description="id do usuario no portal")


class SigninRequest(BaseModel):
    username: str = Field(description="username do usuairo")
    password: str = Field(description="senha do usuario")

class SigninResponse(BaseModel):
    access_token: str = Field(description="Generated access token")
    exp: str = Field(description="Token expiration time")

class UserResponse(BaseModel):
    username: str = Field(description="User username")
    name: str = Field(description="User full name")
    avatar: str = Field(description="User Avatar")
    email: str = Field(description="User email")
    birthday: str = Field(description="User birthday")

"""class SigninResponse(BaseModel):
    access_token: str = Field(description="token de accesso gerado")
    refresh_token: str = Field(description="token para refresh da autenticacao")
    expires_in: int = Field(description="tempo de duração do token")"""