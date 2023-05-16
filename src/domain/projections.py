from pydantic import BaseModel


class ProjectionBase(BaseModel):
    lat_min: float
    lat_max: float
    long_min: float
    long_max: float
    state_province: str

    class Config:
        orm_mode = True


class ProjectionPlace(ProjectionBase):
    state_province: str

