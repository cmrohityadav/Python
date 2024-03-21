class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return self.__brand+ " !"
    def fuel_tye(self):
        return "Petrol or Diesel"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    def fuel_tye(self):
        return "Electric Charge"
my_tesla=ElectricCar("Tesla","Model S","85KWH")


print(my_tesla.fuel_tye())

safari=Car("TATA","Safari")
print(safari.fuel_tye())

