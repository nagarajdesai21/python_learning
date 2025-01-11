from fastapi import FastAPI
from .routers import users, items
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(items.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}