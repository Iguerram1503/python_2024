def solo_fizz_buzz(lista):

    for index, value in enumerate(lista):

        if value % 5 == 0 and value % 3 == 0:

            lista[index] = 'Fizz Buzz'
    
    return(lista)

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#print(solo_fizz_buzz(lista))