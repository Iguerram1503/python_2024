'''
002.Iterables

collecctions: list, tuples, set, dict, son iterables
'''

user_dict ={
    'name' : 'Ibrhim',
    'can_drive' : False,
    'phone' : 5574160522
}

'''
for item in user_dict:
    print(item)

for item in user_dict.items():
    print(item)

for item in user_dict.values():
    print(item)

for item in user_dict.keys():
    print(item)
'''

for item in user_dict.items():
    key, value = item
    print(item)

for key, values in user_dict.items():
    print(key, ':', values)
    