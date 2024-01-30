'''
002 Ejercicio 5

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''

print('Bienvenido al negocio de las inversiones \n') 

cantidad_inversion = int(input('Ingrese la cantidad a invertir: '))

#print(cantidad_inversion)

interes_anual = int(input('Ingrese a cuanto interes porcentual anual le gustaria inertir:  '))

#print(interes_anual)

años_inversion = int(input('Ingrese el numero de años que desea invertir: '))

#print(años_inversion)

for tiempo in range (años_inversion):

    cantidad_final = cantidad_inversion * (1 + (interes_anual / 100)) ** 1

    print(f'La cantidad de inversion al pasar {tiempo + 1} años es de {round(cantidad_final, 2)}')

    cantidad_inversion = cantidad_final


    