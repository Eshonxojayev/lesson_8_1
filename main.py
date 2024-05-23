# Download and Install FASTAPI
"""pip install fastapi uvicorn """

# run fastapi
"""uvicorn main:app --reload"""

from fastapi import FastAPI
from auth import auth_router


app = FastAPI()
app.include_router(auth_router)


@app.get("/")
async def intro():
    return {
        "message": "This is landing page! Created by N37 group"
    }


@app.get("/test")
async def test1():
    return {
        "message": "Hello! Everybody"
    }


@app.get("/test2")
async def test2():
    return {
        "message": "Group -> N37. Hello"
    }
