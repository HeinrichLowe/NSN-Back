from uuid import UUID
from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, field_validator, model_validator
from src.errors.types import HttpBadRequestError

# ----------------------- Signup Schemas -----------------------
class SignupRequest(BaseModel):
    email: str | None = Field(description="email do usuario")
    username: str | None = Field(description="nome do usuario para realizar o login")
    password: str = Field(description="password do usuario para realizar o login")
    full_name: str = Field(description="nome completo (ou não) do usário")
    birthday: str = Field(description="data de nascimento do usário. Ex: 01-01-1999")
    avatar: str | None = Field(description="Profile picture")

    @field_validator("birthday")
    @classmethod
    def valid_bithday(cls, raw):
        date = datetime.strptime(raw, "%Y-%m-%d")
        return date

    @model_validator(mode='after')
    def validate_login_method(self) -> 'SignupRequest':
        if not self.email and not self.username:
            raise HttpBadRequestError("Email or username is required")

        if not self.password:
            raise HttpBadRequestError("Password is required")

        if not self.full_name:
            raise HttpBadRequestError("Name is required")

        if len(self.username) > 32:
            raise HttpBadRequestError("Username too long")

        if len(self.username) < 3:
            raise HttpBadRequestError("Username too short")

        if len(self.password) > 64:
            raise HttpBadRequestError("Password too long")

        if len(self.password) < 6:
            raise HttpBadRequestError("Password too short")

        if len(self.full_name) > 128:
            raise HttpBadRequestError("Name too long")

        return self

class SignupAttributes(BaseModel):
    id: UUID | str = Field(description="ID único do usuário")

class SignupResponse(BaseModel):
    type: str = Field(description="Tipo do objeto")
    count: int = Field(description="Quantidade de itens")
    attributes: SignupAttributes = Field(description="Atriburto de retorno do signup")


# ----------------------- Signin Schemas -----------------------
class SigninRequest(BaseModel):
    email: str | None = Field(description="User Email")
    username: str | None = Field(description="User Username")
    password: str | None = Field(description="User password")

    @model_validator(mode='after')
    def validate_login_method(self) -> 'SigninRequest':
        if not self.email and not self.username:
            raise HttpBadRequestError("Email or username is required")

        if not self.password:
            raise HttpBadRequestError("Password is required")

        return self

#class SigninResponse(BaseModel):
#    access_token: str = Field(description="Generated access token")
#    exp: str = Field(description="Token expiration time")

#class UserResponse(BaseModel):
#    username: str = Field(description="User username")
#    name: str = Field(description="User full name")
#    avatar: str = Field(description="User Avatar")
#    email: str = Field(description="User email")
#    birthday: str = Field(description="User birthday")

#class SigninResponse(BaseModel):
#    access_token: str = Field(description="token de accesso gerado")
#    refresh_token: str = Field(description="token para refresh da autenticacao")
#    expires_in: int = Field(description="tempo de duração do token")


# ----------------------- Search by name Schemas -----------------------
class SearchByNameRequest(BaseModel):
    name: str = Field(description="Nome do usuário para busca")

class SearchByNameAttributes(BaseModel):
    id: UUID | str = Field(description="ID único do usuário")
    full_name: str = Field(default=None, description="Nome completo do usuário")
    avatar: str | None = Field(default=None, description="Avatar do usuário")

class SearchByNameResponse(BaseModel):
    type: str = Field(description="Tipo do objeto")
    count: int = Field(description="Quantidade de itens")
    attributes: List[SearchByNameAttributes] = Field(description="Lista de atributos do usuário")
