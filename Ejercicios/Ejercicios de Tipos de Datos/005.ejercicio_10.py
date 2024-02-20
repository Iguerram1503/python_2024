'''
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
'''

numero_payasos = int(input('Ingresa el numero de juguetes de payaso que se han vendido: '))
numero_muñecas = int(input('Ingresa el numero de juguetes de muñeca que se han vendido: '))

peso_payasos = numero_payasos * 112
peso_muñecas = numero_muñecas * 75

peso_total = peso_muñecas + peso_payasos

print(f'El peso de los payasos es de {peso_payasos}g y el peso de las muñecas es de {peso_muñecas}g porlo tanto el peso total del paquete es de {peso_total}g')