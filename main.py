'''
main Fizz Buzz

'''
from Functions.Verificacion_si_no import verificar_si_no
from Functions.Seleccionar_opcion import seleccionar_opcion
from Functions.Crear_lista import crear_lista
from Functions.Fizz_y_Buzz.solo_fizz import solo_fizz
from Functions.Fizz_y_Buzz.solo_buzz import solo_buzz
from Functions.Fizz_y_Buzz.solo_fizz_buzz import solo_fizz_buzz
from Functions.Fizz_y_Buzz.todo_fizz_buzz import todo_fizz_buzz

print('Bienvenido al programa Fizz Buzz \n')

print('Las reglas son sencillas, vas a ingresar el tamaño de una lista la cual se va a llenar con una numeración de 1 en 1 \n')

print('Posteriormente el programa cada que detecte un multiplo de 3 en la lista va a poner la palabra "Fizz", cuando sea mutiplo de 5 "Buzz" y cuando sea de ambos "Fizz Buzz" \n')

verificar = verificar_si_no()

if verificar == 'S' or verificar == 's':
    print('Comienza el juego \n')

    repetir = 'S'

    while repetir == 'S' or repetir == 's':

        lista_fizz_buzz = crear_lista()
        #print(lista_fizz_buzz)
        print()

        opcion = seleccionar_opcion()

        if opcion == 1:
            print('Selecciono solo "Fizz" \n')

            lista_solo_fizz = solo_fizz(lista_fizz_buzz)

            print(lista_solo_fizz)

        if opcion == 2:
            print('Selecciono solo "Buzz"')

            lista_solo_buzz = solo_buzz(lista_fizz_buzz)

            print(lista_solo_buzz)

        if opcion == 3:
            print('Selecciono solo "Fizz Buzz"')

            lista_solo_fizz_buzz =solo_fizz_buzz(lista_fizz_buzz)

            print(lista_solo_fizz_buzz)

        if opcion == 4:
            print('Selecciono todo')

            lista_completo = todo_fizz_buzz(lista_fizz_buzz)

            print(lista_completo)

        print('\n Se va a repetir todo el proceso')

        repetir = verificar_si_no()

    print('Fin del juego')