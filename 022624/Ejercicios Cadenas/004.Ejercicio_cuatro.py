'''
Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
'''

numero = '+52-5567890234-20'

print('Codigo del pais: ', numero[:3])
print('Numero: ', numero[4:13])
print('Extension: ', numero[15:])