from fastapi import FastAPI
from controllers.slotController import router

app = FastAPI()

app.include_router(router)