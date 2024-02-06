'''
Ejercicio 9
Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.
'''
lista_divisores_uno = []

numero_uno = 10

def maximo_comun_divisor(numero_uno, numero_dos):
    pass

def calcular_divisores_1(numero_uno):
    for numero in range(int((numero_uno / 2 + 1))):
        if numero % numero_uno == 0:
            lista_divisores_uno.append(numero)

calcular_divisores_1(numero_uno)
print(lista_divisores_uno)