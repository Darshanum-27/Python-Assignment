class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def describeVehicleFeatures(self):
        print("This "+str(self.year)+" "+str(self.brand)+" "+str(self.model)+" has "+str(self.mileage)+" miles.")

    def drive(self, miles):
        self.mileage += miles

class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity
        self.charge_level = 100
    
    def BatteryCapacity(self):
        print("Battery capacity: "+str(self.battery_capacity)+" kWh, Charge level: "+str(self.charge_level))

    def batteryChargeLevel(self):
        self.charge_level = 100

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def describeVehicleFeatures(self):
        super().describeVehicleFeatures()
        print("It is a car with "+str(self.doors)+" doors.")


class HybridCar(Car, Electric):
    def __init__(self, brand, model, year, doors, battery_capacity):
        Car.__init__(self, brand, model, year, doors)
        Electric.__init__(self, battery_capacity)

    def describeVehicleFeatures(self):
        super().describeVehicleFeatures()
        self.BatteryCapacity()


class Truck(Vehicle):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity

    def describeVehicleFeatures(self):
        super().describeVehicleFeatures()
        print("It is a truck with a capacity of "+str(self.capacity)+" tons.")


class ElectricTruck(Truck):
    def __init__(self, brand, model, year, capacity, battery_capacity):
        super().__init__(brand, model, year, capacity)
        self.battery_capacity = battery_capacity
        self.charge_level = 100

    def batteryChargeLevel(self):
        self.charge_level = 100

    def BatteryCapacity(self):
        print("Battery capacity:"+str(self.battery_capacity)+" kWh, Charge level: "+str(self.charge_level))


    def describeVehicleFeatures(self):
        super().describeVehicleFeatures()
        self.BatteryCapacity()

# Single Inheritance
my_car = Car('Toyota', 'Corolla', 2017, 4)
my_car.describeVehicleFeatures()
my_car.drive(100)
my_car.describeVehicleFeatures()

# Multiple Inheritance
my_hybrid_car = HybridCar('Rivian', 'Prius', 2022, 4, 8.8)
my_hybrid_car.describeVehicleFeatures()
my_hybrid_car.drive(50)
my_hybrid_car.describeVehicleFeatures()
my_hybrid_car.batteryChargeLevel()
my_hybrid_car.BatteryCapacity()

# Multilevel Inheritance
my_truck = Truck('Peter-Bilt', 'G80', 2022, 2)
my_truck.describeVehicleFeatures()

my_electric_truck = ElectricTruck('Tesla', 'Semi', 2022, 10, 1000)
my_electric_truck.describeVehicleFeatures()
my_electric_truck.drive(200)
my_electric_truck.describeVehicleFeatures()
my_electric_truck.batteryChargeLevel()
my_electric_truck.BatteryCapacity()
