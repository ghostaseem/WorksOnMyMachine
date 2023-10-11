from fastapi import FastAPI
from routers import staff

app = FastAPI()

app.include_router(staff.router)