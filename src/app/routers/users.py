from fastapi import APIRouter


router = APIRouter(
        prefix="/users",
        tags=["users"]
        )


@router.post("/login") 
def user_login(data):
    pass

@router.post("/user") 
def new_user(data):
    pass

@router.delete("/user/{username}") 
def user_delete(username: str):
    pass

@router.post("/logout") 
def user_logout(data):
    pass

