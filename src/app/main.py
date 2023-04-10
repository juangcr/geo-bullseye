from fastapi import FastAPI


app = FastAPI()

@app.get("/find_point") 
def get_polygon(data):
    pass

@app.put("/polygon") 
def get_polygon(data):
    pass

@app.delete("/polygon") 
def get_polygon(data):
    pass

