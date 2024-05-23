from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth")

@auth_router.get("/")
async def auth():
    return {
        "message": "This is auth page"
    }


@auth_router.get("/login")
async def login():
    return {
        "message": "This is login page"
    }

@auth_router.get("/logout")
async def logout():
    return {
        "message": "This is logout page"
    }


@auth_router.get("/register")
async def register():
    return {
        "message": "This is register page"
    }