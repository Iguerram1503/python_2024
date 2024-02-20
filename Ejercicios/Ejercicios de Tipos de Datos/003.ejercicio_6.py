'''
Ejercicio 6
Escribir un programa que lea un entero positivo "n" introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta "n".
'''

numero = int(input('Ingrese un número entero positivo: '))

suma_enteros = int(numero * (numero + 1) / 2)

print(suma_enteros)