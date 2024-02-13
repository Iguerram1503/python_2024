def learning_python():
    print('Learning Python')

def calcular_iva(cantidad_pagar, iva_pagar=21):
    '''
    Info: Esta funcion recibe una cantidad a pagar ingresada por el usuario y un impuesto que se debe sumar a la cantidad anterior, (De no ser especificado se considerará un IVA del 21%)\n
    Posteriormente devolvera una factura en la que se indique la cantidad a pagar incluyendo el IVA\n
    Ingresa:
        - int: cantidad_pagar
        - int: iva_pagar\n
    Regresa
        - str: factura_total
    '''

    iva_porcentaje = iva_pagar / 100

    cantidad_iva = cantidad_pagar * iva_porcentaje

    cantidad_total = round(cantidad_pagar + cantidad_iva, 2)

    return f'El precio a pagar es de {cantidad_pagar} mas un IVA de {iva_pagar}% da un total de {cantidad_total}'

#print(calcular_iva(100, 15))

def lista_uno_ej_7(lista_uno):

    '''
    Esta funcion recibe una lista con numeros ingresados por el usuario\n
    
    Posteriormente genera una lista en la que se van anexando los numeros elevadoss al cuadrardo que se encuentran en la primera lista\n
    
    Ingresa: 
        - List: lista_numeros\n
    Regresa:
        - List: lista_cuadrados
    '''

    lista_dos = []

    for numero in lista_uno:

        lista_dos.append(numero ** 2)
    
    return lista_dos

