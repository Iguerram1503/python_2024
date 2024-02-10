def solo_fizz(lista):

    for index, value in enumerate(lista):

        if value % 3 == 0:

            lista[index] = 'Fizz'
    
    return(lista)

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print(solo_fizz(lista))