'''
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
'''

nombre = input('Ingrese su nombre: ')
repeticiones = int(input('Ingrese cuantas veces desea repetir su nombre: '))

for repeticion in range (repeticiones):
    print(nombre)