import uuid
from typing import Dict, List, Optional
from .models import User, Booking
from .security import hash_password

USERS: Dict[str, User] = {
    "admin": User("admin", hash_password("admin123"), True),
    "alice": User("alice", hash_password("alice123"), False),
}

BOOKINGS: Dict[str, Booking] = {}

def next_id() -> str:
    return uuid.uuid4().hex

def add_booking(owner: str, slot: str) -> Booking:
    b = Booking(next_id(), owner, slot)
    BOOKINGS[b.id] = b
    return b

def get_booking(bid: str) -> Optional[Booking]:
    return BOOKINGS.get(bid)

def delete_booking(bid: str) -> None:
    BOOKINGS.pop(bid, None)

def list_all() -> List[Booking]:
    return list(BOOKINGS.values())

def list_by_owner(owner: str) -> List[Booking]:
    return [b for b in BOOKINGS.values() if b.owner == owner]
