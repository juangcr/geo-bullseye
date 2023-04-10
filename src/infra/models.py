from database import Base
from sqlalchemy import Column, Boolean, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)


class Polygons(Base):
    __tablename__ == "polygons"

    id = Column(Integer, primary_key=True, index=True)
    lat = Column(Float)
    long = Column(Float)
    state_province = Column(String)
    country = Column(String)

    projections = relationship("Projections", back_populates="polygons")


class Projections(Base):
    __tablename__ == "projections"

    id = Column(Integer, primary_key=True, index=True)
    lat_min = Column(Float)
    lat_max = Column(Float)
    long_min = Column(Float)
    long_max = Column(Float)
    state_province = Column(String, ForeignKey("polygons.state_province"))

    polygons = relationship("Polygons", back_populates="projections")

