class vehicle:

    # class attribute (shared)
    wheel: int = 4

    # constructor
    def __init__(self, plate, owner):
        # Instance Attributes
        self.plate = plate 
        self.owner = owner
        self._mileage = 0 # private

    # Instance method
    def drive (self, km):
        if km < 0:
            raise ValueError("km must be non-negative")
        self._mileage += km

    @property
    def mileage(self):
        return self._mileage
    
    def __repr__(self):
        return f"Vehicle(Plate: {self.plate!r}, Mileage {self._mileage})"
    
    def __eq__(self, other):
        return isinstance(other, vehicle) and self.plate == other.plate

# Inheritance
class Truck(vehicle):
    wheel = 6

    def __init__(self, plate, owner, capacity):
        super().__init__(plate, owner)
        self.capacity = capacity

# Instaciation
t = Truck("Dhaka Metro 24124", "Tahmid", 5000)
t.drive(205)
# print(repr(t))
print(t)
t_another = Truck("Chatto Metro 54334", "Habib", 7253)
# print(t.__eq__(t_another))
print (t == t_another)
t_another.drive(123)
print(t_another._mileage)