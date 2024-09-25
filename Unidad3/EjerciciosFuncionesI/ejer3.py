# 3. Escribir una función que calcule el total de una factura tras aplicarle el
# IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a
# aplicar, y devolver el total de la factura. Si se invoca la función sin
# pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calcula_iva(sinIVA,porcentaje=21):
    porcentaje = (100 - porcentaje) /100
    total = sinIVA * porcentaje
    return total

print(f"El importe total con el IVA calculado es: {calcula_iva(100,20)}")
