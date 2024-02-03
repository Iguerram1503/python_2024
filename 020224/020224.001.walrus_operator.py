'''
001 Walrus operator
" := " 
- Permite asignar una variable y al mismo tiempo devolver el valor
- Entró en la version 3.8 de python 
'''
'''
name = 'Ibrahim'
print(name)
print(type(name))

print(second_name := 'Iguerram')
print(type(second_name))

lista = []
entrada = input('Escribe algo: ')

while entrada != 'fin':
    lista.append(entrada)
    entrada = input('Escribe algo: ')

print(lista)
'''

lista = []

while(entrada := input('Escribe algo: ')) != 'fin':
    lista.append(entrada)

print(lista)