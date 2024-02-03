'''
001 args se usa para funciones
- *args: Nos ayuda a pasar cualquier número de argumentos en una función, estos se convierten en una tupla
- Regla: 1.argumentos / parametros
         2. *args
         3. default params
         4. **kwards
'''
'''
def suma(valor_uno, valor_dos):
    print(valor_uno + valor_dos)

suma(8,8,9) #Nos despliega error porque ponemos mas argumento 
'''

#*args nos permite agregar tantos parametros como sean 
    
def suma_calificaciones(*args):
    #Los argumentos los convierte en tuplas
    print(args)
    print(type(args))
    resultado = 0
    for valores in args:
        resultado += valores
    return resultado

print(suma_calificaciones(8, 10, 9, 6, 8, 7, 10))