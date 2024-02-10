def todo_fizz_buzz(lista):

    for index, value in enumerate(lista):

        if value % 5 == 0 and value % 3 == 0:

            lista[index] = 'Fizz Buzz'

        elif value % 5 == 0:

            lista[index] = 'Buzz'

        elif value % 3 == 0:

            lista[index] = 'Fizz'
    
    return(lista)

#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

#print(todo_fizz_buzz(lista))