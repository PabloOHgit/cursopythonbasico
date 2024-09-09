#Ejercicio 2: Creo un programa para calcular la suma de números que introduzca
#el usuario por pantalla hasta que ingrese 0.

num1 = 1
num2 = 1
print("Vamos a sumar dos números que introduzcas hasta que ingreses un 0 ")
while(num1 != 0 and num2 != 0):
    num1 = int(input("\nIntroduce un primer número para la suma "))
    num2 = int(input("\nIntroduce el segundo número para sumar al primero "))
    print("\nEl resultado de la suma es",num1 + num2)
else:
    print("\nHEMOS TERMINADO.Has introducido un 0 en algún sumando")