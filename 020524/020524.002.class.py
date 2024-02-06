'''
Class: HUMAN

- Attributes: 
    . Lugar de nacimiento  
    . Fecha de nacimiento 
    . Color
    . Raza
    . Religión

- Methods:
    . Camina
    . Corre
    . Habla
    . Duerme
    . Come
    . Siente
'''
#Nombre de la clase en mayúscula
class Persona: 
    
    #Atributos
    first_name = ''
    last_name = ''
    born_year = ''

    #métodos

    def say_hello(self):
        return 'Hello'
    
    def say_bye(self):
        return 'Bye'
    
#instanciar = crear 
    
persona_uno = Persona()
persona_uno.first_name = 'Ibrahim'
persona_uno.last_name = 'Guerra'
persona_uno.born_year = 2007

#invoke = llamar un metodo

print(persona_uno.first_name)
print(persona_uno.last_name)
print(persona_uno.born_year)
print(persona_uno.say_hello())
print(persona_uno.say_bye())

persona_dos = Persona()
persona_dos.first_name = 'Maggie'
print(persona_dos.first_name)

persona_tres = Persona()
persona_tres.first_name = 'Ibra'
print(persona_tres.first_name)
