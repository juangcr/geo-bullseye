from fastapi import FastAPI
from routers import coordinates, users
from database import engine



models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(coordinates.router)
app.include_router(users.router)



