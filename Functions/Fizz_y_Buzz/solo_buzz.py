def solo_buzz(lista):

    for index, value in enumerate(lista):

        if value % 5 == 0:

            lista[index] = 'Buzz'
    
    return(lista)

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print(solo_buzz(lista))