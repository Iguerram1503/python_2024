def say_hello_user(user):
    print(f'Hello {user}')

def decorator_argument(function):

    def internal(argument):

        print('-----------------')
        function(argument)
        print('-----------------')
    return internal

@decorator_argument
def say_bye_user(user_name):
    print(f'Bye {user_name}')