'''
002.Condicionales
-if
-else
-elif

-and Ambas deben de ser true
-or Al menos una tiene que ser veradera
'''

is_old = False
driver_licence = False

'''
if is_old == True:
    print('Tienes edad para manejar')
elif driver_licence:
    print('Puedes conducir')
else:
    print('No tienes edad para manejar')


if is_old and driver_licence:
    print('Eres un buen ciudadano con licencia y la edad suficiente')
else:
    print('Lo siento, no puedes conducir')

if is_old or driver_licence:
    print('Puedes conducir')
else:
    print('No puedes conducir')


edad = int(input('Cuál es tu edad? '))

if edad >= 18 and edad <= 70:
    print('Eres mayor de edad')
elif edad > 71:
    print('Aun que eres mayor de edad, dudo que puedas manejar')
else:
    print('Que estas haciendo? ')
'''

user = input('User: ')
password = input('Password: ')

if user == 'Ibrahim' and password == '123':
    print('Acceso a la aplicación')
else:
    print('Usuario o contraseña incorrectos')

