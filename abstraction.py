from abc import ABC, abstractmethod


# Abstract Class
class Device(ABC):
    def __init__(self, device_id: str, brand: str, model: str):
        self._device_id = device_id
        self._brand = brand
        self._model = model

    @abstractmethod
    def calculate_power_consumption(self) -> float:
        pass

    @abstractmethod
    def calculate_maintenance_cost(self) -> float:
        pass

    @abstractmethod
    def getDetails(self) -> str:
        pass



class Laptop(Device):
    def __init__(self, device_id: str, brand: str, model: str, processor_power: float, daily_usage_hours: float, maintenance_cost_per_year: float):
        super().__init__(device_id, brand, model)
        self.processor_power = processor_power
        self.daily_usage_hours = daily_usage_hours
        self.maintenance_cost_per_year = maintenance_cost_per_year

    def calculate_power_consumption(self) -> float:
        return (self.processor_power * self.daily_usage_hours * 365) / 1000

    def calculate_maintenance_cost(self) -> float:
        return self.maintenance_cost_per_year

    def getDetails(self) -> str:
        return f"Device ID: {self._device_id}, Brand: {self._brand}, Model: {self._model}"


laptop = Laptop("LAP123", "Dell", "XPS 13", 30.0, 8.0, 150.0)

print("Device Details:")
print(laptop.getDetails())

print("Power Consumption (kWh):")
print(laptop.calculate_power_consumption())

print("Maintenance Cost ($):")
print(laptop.calculate_maintenance_cost())
