'''
001.List
Una lista es un tipo de variable que permite almacenar varios datos 
'''

list_my_students = ['Maggie', 'Ibrahim', 'Paulina', 'Octavio', 'Ulises']

print(list_my_students)
print(list_my_students[0])
print(list_my_students[1])
print(list_my_students[2])
print(list_my_students[3])
print(list_my_students[4])

print('\n\n')

print('".append"')
list_my_students.append('Luis')
print(list_my_students)
list_my_students.pop()

print('\n\n')

print('".insert"')
list_my_students.insert(0, 'Isela')
print(list_my_students)
list_my_students.remove('Isela')

print('\n\n')

print('".pop"')
print(list_my_students)
list_my_students.pop()
print(list_my_students)
list_my_students.pop(1)
print(list_my_students)

list_my_students.insert(1, 'Ibrahim')
list_my_students.insert(4, 'Ulices')

print('\n\n')

print('".remove"')
print(list_my_students)
list_my_students.remove('Paulina')
print(list_my_students)

list_my_students.insert(3, 'Paulina')

print('\n\n')

print('List with another type of data')
list_my_students.append(2024)
list_my_students.append(2.50)
print(list_my_students)

list_my_students.pop()
list_my_students.pop()