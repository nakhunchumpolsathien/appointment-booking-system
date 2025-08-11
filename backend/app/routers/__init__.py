from fastapi import APIRouter
from .auth import router as auth_router
from .bookings import router as bookings_router

api = APIRouter()
api.include_router(auth_router)
api.include_router(bookings_router)
