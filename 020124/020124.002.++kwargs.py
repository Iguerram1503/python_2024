'''
002 kwargs
- Diccionario
'''

def estudiante(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(len(kwargs))


estudiante(first_name='Ibrahim', last_name='Guerra')