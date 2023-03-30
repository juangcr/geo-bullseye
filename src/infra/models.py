from database import Base
from sqlalchemy import Column, Boolean, String, Integer, Float


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)



class Projections(Base):
    __tablename__ == "projections"

    proj_id = Column(Integer, primary_key=True, index=True)
    lat_min = Column(Float)
    lat_max = Column(Float)
    long_min = Column(Float)
    long_max = Column(Float)
    state_province = Column(String)


class Polygons(Base):
    __tablename__ == "polygons"

    poly_id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    long = Column(Float)
    state_province = Column(String)
    country = Column(String)

