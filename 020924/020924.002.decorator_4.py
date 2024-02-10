user1 = {

    'name': 'Maggie',
    'valid': True
}

user2 = {

    'name': 'Ibrahim',
    'valid': False
}

def authenticated(function):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return function(*args, **kwargs)
        else:
            return print('Invalid user')
        
    return wrapper

@authenticated
def message_frien(user):

    print('Message has been send to your friend')

message_frien(user1)