'''
001 Functions
- Bloques de coodigo que pueden ser reutilizados y llamados
- Pueden o no recibir parametro
'''

'''
def say_hello():
    print('Hello')

say_hello()

def say_hello_user(user_name):
    print(f'Hello {user_name}')

say_hello_user('Ibrahim')
'''

def say_hello_user(user_name):
    return f"Hello {user_name}"

print(say_hello_user('Ibrahim'))