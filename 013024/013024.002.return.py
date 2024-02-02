'''
002 Return
- Todas las funciones regresan algo
- No todas imprimen algo
- Una funcion debe de hace una cosa, bien
- al aplicar el "return" sales de la funcion
'''

def convertir_porcentaje(valor):
    resultado = valor / 100
    return resultado

def redondeo_dos_decimales(valor, decimales=2):
    return round(valor, decimales)

def calcular_monto_propina(monto_pagar, porcentaje_propina):
    monto_propina = monto_pagar * porcentaje_propina
    return monto_propina

def cantidad_total(monto_consumo, monto_propina):
    total = monto_consumo + monto_propina
    return f"Monto de consumo ${monto_consumo}, monto de propina ${monto_propina}, total a pagar ${redondeo_dos_decimales(total)}"

#--------------------------------------------------------------------------------------

consumo = float(input("Consumo: "))
propina = float(input("Propina: "))

porcentaje = convertir_porcentaje(propina)

monto_propina = calcular_monto_propina(consumo, porcentaje)

print(cantidad_total(consumo, monto_propina))


