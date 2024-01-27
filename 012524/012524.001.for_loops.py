'''
001.For loops
- Es una iteración
'''
'''
course = 'Learning Python'

for letter in course:
    print(letter)

my_students_list = ['Paulina', 'Ulises', 'Octavio', 'Maggie', 'Ibrahim']

for student in my_students_list:
    print(student)

my_numbers_set = {10, 20, 30, 40, 50}

for number in my_numbers_set:
    print(number)

my_numbers_tuple = (10, 20, 30, 40, 50)

for i in my_numbers_tuple:
    print(i)
'''

my_numbers_list = [1, 2, 3, 4, 5]
my_letter_list = ['a', 'b', 'c', 'd', 'e']

for number in my_numbers_list:
    for letter in my_letter_list:
        print('-----')
        print(number, letter)