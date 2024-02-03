'''
003 Global Keyword
- Nos permite llamar a una variable global dentro de una función donde la variable es local'''

#global
total = 100

def print_total():
    total = 1
    total += 1
    print(total)

print_total()

def print_total_2():
    global total
    total += 1
    print(total)

print_total_2()