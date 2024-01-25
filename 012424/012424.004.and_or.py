'''
004.and y or

and: Ambos valores deven de ser verdaderos (True)
or: al menos un valor debe ser verdadero (True)

'''

is_employed = True

is_developer = True

employed_state = 'Eres de IT' if is_employed and is_developer else 'Eres administrativo'

print(employed_state)