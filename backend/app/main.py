from fastapi import FastAPI
from .routers import api

app = FastAPI(title="Appointment API")
app.include_router(api)

@app.get("/")
def root():
    return {"message": "OK"}