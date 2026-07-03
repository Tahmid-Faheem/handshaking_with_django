class VehicleNorFoundError(Exception):
    """Raised when a vehicle look up fails."""

def get_car(plate):
    db = {"Dhaka 245": {"Owner": "Tahmid"}}
    try:
        return db[plate]
    except KeyError as e:
        raise VehicleNorFoundError(f"plate = {plate}") from e
    
try:
    v = get_car("Dhaa 245")
except VehicleNorFoundError as e:
    print("Handled", e)
finally:
    print("Cleanup runs always")