'''
003 Lambda
- Son funciones anónimas
- puede tomar cualquier numero de argumentos, pero solo tiene una expresion
- El resultado se guarda en una variable
'''

def suma(numero):
    resultado = numero + 1
    return resultado

#print(suma(1))

resultado = lambda numero: numero + 1
#print(resultado(1))

resultado_dos = lambda numero_uno, numero_dos: numero_uno + numero_dos + 1
print(resultado_dos(2, 2))