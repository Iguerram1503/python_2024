'''
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de pesos y el número de centavos del precio introducido.
'''

precio = input('Introduce una cantidad de dinero')
print(precio[:precio.find('.')], 'pesos y', precio[precio.find('.')+1:])