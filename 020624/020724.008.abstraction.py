'''
008 Abstraccion 
'''

class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model  

    def drive(self):
        pass

vehicle_one = Vehicle
print(vehicle_one)

class Car(Vehicle):

    def drive(self):
        return f'Conduciendo en la ciudad un {self.brand} del modelo {self.model}'

class Truck(Vehicle):

    def drive(self):
        return f'Conduciendo en el campo, mi {self.brand} modelo {self.model }'

class Motorcicle(Vehicle):

    def drive(self):
        return f'Conduciendo mi moto {self.brand} modelo {self.model} en la pista '

car_one = Car('VW', 'Jetta')
print(car_one.drive())
print(car_one.drive)

car_two = Truck('Ford', 'Lobo')
print(car_two.drive())
print(car_two.drive)

car_three = Motorcicle('Duckaty',  '848 evo')
print(car_three.drive())