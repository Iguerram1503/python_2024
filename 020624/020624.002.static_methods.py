'''
002 static methods

Los metodos estaticos pueden ser accesibles sin instanciar un objeto, solo se necesita llamar a la clase 
'''

class Student:

    def __init__(self, id, full_name):
        self.id = id
        self.full_name = full_name

    def speak(self):
        return 'Speaking'
    
    def walk(self):
        return 'Walking'
    
    @staticmethod
    def run():
        return 'Running'
    
    @classmethod
    def sleep(cls, starting, end):
        return f'slepping from {starting} to {end}'

ibrahim = Student('100', 'Ibrahim Guerra')

print(ibrahim.speak())
#print(ibrahim.run())

print(Student.sleep('10:00', '7:00'))

