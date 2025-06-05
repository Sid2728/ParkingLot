from fastapi import FastAPI
from app.controllers.slotController import router

app = FastAPI()

app.include_router(router)