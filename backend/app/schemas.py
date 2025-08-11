from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class BookingCreate(BaseModel):
    slot: str

class BookingUpdate(BaseModel):
    slot: str

class BookingOut(BaseModel):
    id: str
    owner: str
    slot: str
