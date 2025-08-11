from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    username: str
    password_hash: str
    is_admin: bool

@dataclass
class Booking:
    id: str
    owner: str
    slot: str
