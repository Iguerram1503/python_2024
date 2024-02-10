def verificar_si_no():
    '''
    Info: Esta funcion pide al usuario una respuesta, ya sea "s" o "n", si no recibe ninguna de las anteriores no permite seguir avanzando \n
    Ingresa:
        - str: respuesta_usuario \n
    Regresa:
        - str: respuesta_verificada

    '''
    respuesta = input('Desea continuar? s/n ')

    while respuesta != 's' and respuesta != 'S' and respuesta != 'n' and respuesta != 'N':
        print('Entrada no valida \n')
        respuesta = input('Ingresa "s" o "n" ')
        print()
    
    return respuesta

#verificar_si_no()