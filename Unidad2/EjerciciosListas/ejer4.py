# Ejercicio 4. Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46,
# 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

lista_precios = [50,75,46,22,80,65,8]

lista_precios.sort()
print(f"El menor de los números es: {lista_precios[0]}")

lista_precios.reverse()
print(f"El mayor de los números es: {lista_precios[0]}")

# Otro método
print(lista_precios[0])
print(lista_precios[-1])

# Otro método
num = len(lista_precios)
print(lista_precios[num - 1])

# Otro método
# Calcular el menor y el mayor precio
menor_precio = min(lista_precios)
mayor_precio = max(lista_precios)

# Mostrar los resultados
print(f"El menor precio es: {menor_precio}")
print(f"El mayor precio es: {mayor_precio}")
    