from pydantic import BaseModel


class Users(BaseModel):
    user_id: int
    user_name: str
    password: str
    admin: bool


class Projections(BaseModel):
    proj_id: int
    lat_min: float
    lat_max: float
    long_min: float
    long_max: float
    state_province: str


class Polygons(BaseModel):
    poly_id: int
    lat: float
    long: float
    state_province: str
    country: str
