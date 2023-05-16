from fastapi import APIRouter, Depends, status, HTTPException
from src.domain import polygons
from src.infra import models

router = APIRouter(
        prefix="/coordinates",
        tags=["coordinates"]
        )

@app.get("/find_point") 
def get_polygon(
    data: polygons.FindCoordinates,
    db: Session = Depends(database.get_db)):
    # Find point in projections table.
    # If found, return state_province.
    # If many, use PiP algo and return results.
    pass


@app.put("/new") 
def put_polygon(
    data: polygons.InsertPolygon,
    db: Session = Depends(database.get_db)):
    existing_polygon = db.query(models.Polygons)
    .filter(models.Blog.country == country)
    .filter(models.Blog.state_province == state_province)
    if not existing_polygon.first():
        db.add()
    pass


@app.delete("/{state_province}") 
def delete_polygon(
    state_province: str,
    db: Session = Depends(database.get_db)):
    pass
