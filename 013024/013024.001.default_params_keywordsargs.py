'''
001.Default params and keywords
'''

'''
#def say_hello_usser_phone(user_name, user_phone):
    #print(f'Hello user {user_name}, you can call me {user_phone}')


#possitional
#say_hello_usser_phone('Ibrahim', '5574160522')
#say_hello_usser_phone('5574160522', 'Ibrahim')

#keywords arguments, es decile explicitamente, que cada valor no tiene una posicion, ya que será asignado
    
say_hello_usser_phone(user_name='Luis', user_phone='5574160522')
say_hello_usser_phone(user_phone='5574160522', user_name='Luis')
'''

def say_hello_usser_phone(user_name='Paulina', user_phone='3329372934'):
    print(f'Hello user {user_name}, you can call me {user_phone}')

say_hello_usser_phone()
say_hello_usser_phone('Ibrahim', '5574160522')
say_hello_usser_phone('5574160522', 'Ibrahim')