from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    admin: bool


class UserResponse(User):
    username: str

    class Config:
        orm_mode = True


