"""Python is dynamically typed. Still we need type hint. Those don't force the type though. """
# Wroks, as cpython directly ignores type hint
def fetch_age(name: str) -> int:
    return "This is a string."

print(fetch_age("Thamid"))

# Not too modern way but fine
from typing import Optional, Iterable

def find_user(user_id: int) -> Optional[dict]:
    db = {1: {"name": "Tahmid"}}
    return db.get(user_id)

print(find_user(1))

# Modern way
def sells(id: int) -> dict | None:
    db = {12: {"Name": "Wholesell"}}
    return db[12]

# Dataclass as shortcut of large classes
from dataclasses import dataclass

@dataclass
class GPSpoints:
    lat:float
    long: float
    timestamp: float
    speed: float = 0.0

v = GPSpoints(1,23,65,45)
print(v)