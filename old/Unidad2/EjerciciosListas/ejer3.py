# Ejercicio 3. Escribir un programa que almacene en una lista con 10 números y los ordene de
# mayor a menor.

orden_nums = []

for i in range(10):
    orden_nums.append(int(input("Introduce un número de 10: ")))

orden_nums.sort()
orden_nums.reverse()
# Otra forma de hacerlo 
# orden_nums.sort(reverse=True)
print(orden_nums)