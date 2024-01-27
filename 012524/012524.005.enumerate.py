'''
005.enumerate

'''

'''
course = 'Learning Python'

for index, character in enumerate(course):
    #print(index, character)
    if character == 'i':
        print(f'Index of {character} in possition {index}')
'''

my_courses = ['Python', 'Scrum', 'Docker', 'NGINX']

'''
for index, course in enumerate(my_courses):
    print(index, course)
    find = input('find: ')
    if find == index:
        print(f'Course {course} found in index {index}')
'''

for index, course in enumerate(my_courses):
    print(index, course)

find = input('Ingresa el nombre del curso que desea conocer: ') 

for index, course in enumerate(my_courses):
    if find == course:
        print(f'Curso {course} encontrado en el índice {index}')
        print('Desplegando la información correspondiente')



