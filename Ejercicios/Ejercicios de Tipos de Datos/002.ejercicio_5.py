'''
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.
'''

horas_trabajadas = int(input('Ingrese el numero de horas que trabajó: '))

paga_hora = int(input('Ingrese cuanto dinero le pagan por hora: '))

paga_total = horas_trabajadas * paga_hora

print(f'Usted trabajó {horas_trabajadas} horas, por lo tanto su paga es de {paga_total}$')