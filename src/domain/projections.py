from pydantic import BaseModel


class ProjectionBase(BaseModel):
    lat_min: float
    lat_max: float
    long_min: float
    long_max: float
    state_province: str


class ProjectionLat(ProjectionBase):
    lat_min: float
    lat_max: float


class ProjectionLong(ProjectionBase):
    long_min: float
    long_max: float


class ProjectionPlace(ProjectionBase)
    state_province: str

