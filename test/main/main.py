def suma_cinco(numero):
    try:
        if numero:
            return numero + 5
        else:
            return 'Por favoer inresa un numero'
    except ValueError as error:
        return error

    

#print(suma_cinco(1))

#assert(suma_cinco(1) == 6)
#assert(suma_cinco(1) == 1)