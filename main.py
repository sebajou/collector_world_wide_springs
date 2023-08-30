import uvicorn
from typing import List

from fastapi import FastAPI, HTTPException

import config
from database import MongoDB
from models import Spring

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.on_event("startup")
async def on_startup():
    await MongoDB.init(config.MONGO_URI, config.MONGO_DB_NAME)


@app.post("/springs", response_model=Spring)
async def create_spring(spring: Spring):
    await spring.insert()
    return spring


@app.get("/springs", response_model=List[Spring])
async def read_springs():
    springs = await Spring.find_all().to_list()
    return springs


@app.get("/springs/{spring_id}", response_model=Spring)
async def read_spring(spring_id: str):
    spring = await Spring.find_one({"id": spring_id})
    if not spring:
        raise HTTPException(status_code=404, detail="Spring")


@app.put("/springs/{spring_id}", response_model=Spring)
async def update_spring(spring_id: str):
    # spring = await Spring.find_one({"id": spring_id})
    spring = await Spring.update_one({"id": spring_id})
    if not spring:
        raise HTTPException(status_code=404, detail="Spring")


if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
