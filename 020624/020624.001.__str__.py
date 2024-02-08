'''
001 __str__

'''

class Car:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self):
        return f'This as {self.brand} {self.model} color {self.color}'

#instanciando 
jetta = Car('VW', 'Jetta', 'Blanco')

print(jetta)

ibiza  = Car('Seat', 'Ibiza', 'Rojo')

print(ibiza)