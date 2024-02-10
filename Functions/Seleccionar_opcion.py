def seleccionar_opcion():
    '''
    Esta función le pide al usuario elegir una opcion del 1 al 4, si no se cumple este requerimiento no permite avanzar\n
    Ingresa:
        - int: opcion_usuario
    Regresa:
        - int: opcion_verificada
    '''

    print('Ingrese que desea ver del programa\n')
    print('1. Solo "Fizz"')
    print('2. Solo "Buzz"')
    print('3. Solo "Fizz Buzz"')
    print('4. Todo \n')

    opcion = int(input('Selecciona la opcion que guste.  '))

    while opcion < 1 or opcion > 4:

        print('Entrada no valida. \n')
        opcion = int(input('Igrese un numero entre 1 y 4. '))
        print()
    
    return opcion

#seleccionar_opcion()