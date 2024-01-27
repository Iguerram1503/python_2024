'''
006. While
'''

iterador = 0

'''
while iterador < 5:
    print(iterador)
    iterador += 1

print('Done')
'''

option = 0

while option != '3':
    print('1. Revisar saldo')
    print('2. Retirar')
    print('3. Salir')
    option = input('Ingrese una opción: ')
    if option == '3':
        input('Dentro del if')
    