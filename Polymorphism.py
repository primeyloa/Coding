from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id: str, model: str, fuel_level: float):
        super().__init__()
        self.vehicle_id = vehicle_id
        self.model = model
        self.fuel_level = fuel_level

    def refuel(self, liters: float):
        self.fuel_level += liters
        print(f"Refueled {liters} liters. Updated fuel level: {self.fuel_level} liters.")

    @abstractmethod
    def calculate_range(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_id: str, model: str, fuel_level: float, fuel_efficiency: float):
        super().__init__(vehicle_id, model, fuel_level)
        self.fuel_efficiency = fuel_efficiency

    def calculate_range(self):
        range = self.fuel_level * self.fuel_efficiency
        print(f"Car {self.model} can travel {range} km with current fuel level.")


class TransportationManager:
    @staticmethod
    def operate_vehicle(vehicle: Vehicle):
        vehicle.calculate_range()


car1 = Car("001", "Salon", 90, 15)

car1.refuel(10)

manager = TransportationManager()
manager.operate_vehicle(car1)
