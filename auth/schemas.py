from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class UserRegistration(BaseModel):
    username: str
    email: str
    password: str



class UserLogin(BaseModel):
    username: str
    password: str


class UserProfile(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True