'''
004 Inheritance

'''

class Human:

    def __init__(self, name, born_year):
        self.name = name
        self.born_year = born_year

    def walk(self):
        return 'Walking'

human_one = Human('Luis', 1945)

print(human_one.name)
print(human_one.born_year)

class Man(Human):
    
    def __init__(self, name, born_year, last_name):
        super().__init__(name, born_year)
        self.last_name = last_name
        

ibrahim = Man('Ibrahim', 2022, 'Guerra')

print(ibrahim.name)
print(ibrahim.born_year)
print(ibrahim.walk())