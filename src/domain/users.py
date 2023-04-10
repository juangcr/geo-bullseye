from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    admin: bool
    is_active: bool


class UserResponse(User):
    username: str
    admin: bool
    is_active: bool

    class Config:
        orm_mode = True


