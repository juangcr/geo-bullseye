from pydantic import BaseModel


class Polygons(BaseModel):
    lat: float
    long: float
    state_province: str
    country: str
    
    class Config:
        orm_mode = True
