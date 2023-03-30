from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    admin: bool
    is_active: bool

    class Config:
        orm_mode = True


class ProjectionBase(BaseModel):
    pass


class ProjectionLat(ProjectionBase):
    lat_min: float
    lat_max: float


class ProjectionLong(ProjectionBase):
    long_min: float
    long_max: float


class ProjectionPlace(ProjectionBase)
    state_province: str


class Projection(ProjectionBase)
    proj_id: int

    class Config:
        orm_mode = True


class Polygons(BaseModel):
    poly_id: int
    lat: float
    long: float
    state_province: str
    country: str
