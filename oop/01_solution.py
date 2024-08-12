class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"Car name is test, brand: {self.__brand} and model: {self.__model}"

    def get_brand(self):
        return self.__brand
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


class Battery:
    def battery_info(self):
        return "This is battery"


class Engine:
    def engine_info(self):
        return "This is engine"
        
class ElectricCarTwo(Battery, Engine, Car):
    pass




tesla = ElectricCarTwo("Tesla", "Model S")

print(tesla.battery_info())