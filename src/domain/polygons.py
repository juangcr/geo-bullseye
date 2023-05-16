from typing import List
from pydantic import BaseModel


class PolygonBase(BaseModel):
    lat: float
    long: float
    state_province: str
    country: str
    
    class Config:
        orm_mode = True


class FindCoordinates(PolygonBase):
    lat: float
    long: float
    

class StateProvince(PolygonBase):
    state_province: str


class InsertPolygon(BaseModel):
    state_province: str
    country: str
    coordinates: List[FindCoordinates]

    class Config:
        orm_mode = True

