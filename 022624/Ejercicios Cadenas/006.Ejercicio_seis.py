'''
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''

frase = input('Ingresa una frase: ')

vocal = input('Ingresa la vocal que desea poner en mayuscula: ')
vocal_mayus = vocal.upper()

print(frase.replace(vocal, vocal_mayus))