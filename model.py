from fastapi import APIRouter



model_router = APIRouter(prefix="/model", tags=["model"])

@model_router.post("/")
async def model():
    return {
        "message": "model page"
    }


@model_router.get("/model1")
async def model_1():
    return {
        "message": "model 1"
    }


@model_router.get("/model2")
async def model_2():
    return {
        "message": "model 2"
    }