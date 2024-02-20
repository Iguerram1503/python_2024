'''
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.
'''

numerador = int(input('Ingresa el dividendo de la división: '))
denominador = int(input('Ingresa el divisor de la división: '))

cociente = round(numerador / denominador, 2)
resto = numerador % denominador

print(f'La división de {numerador} entre {denominador} da un cociente de {cociente} y un resto de {resto}')