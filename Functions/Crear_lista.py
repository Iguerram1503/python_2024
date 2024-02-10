def crear_lista():
    '''
    Esta función se encarga de generar la lista que se va a ocupar para el juego Fizz Buzz \n

    Ingresa:
        - int: tamaño_lista \n
    Regresa:
        - lista: lista_juego
    '''

    print('Ingresa los datos que se piden a continuación \n')

    tamaño_lista = int(input('Ingrese hasta que numero desea ver en el programa.  '))

    lista_fizz_buzz = []

    for numero in range(1, (tamaño_lista + 1)):

        lista_fizz_buzz.append(numero)

    return lista_fizz_buzz

#print(crear_lista())