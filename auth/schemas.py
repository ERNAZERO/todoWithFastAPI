from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserRegistration(BaseModel):
    username: str
    email: str
    password: str
    full_name: str


class UserLogin(BaseModel):
    username: str
    password: str