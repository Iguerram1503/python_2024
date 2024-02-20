'''
Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
'''

barras = int(input("Introduce el número de barras vendidas que no son del dia: "))
precio = 3.49 
descuento = 0.6
coste = round(barras * precio * (1 - descuento), 2)
print(f'El coste de una barra fresca es {precio}$')
print(f'El descuento de una barra por no se del dia es de {descuento * 100}%')
print(f'El coste final a pagar es {coste}')