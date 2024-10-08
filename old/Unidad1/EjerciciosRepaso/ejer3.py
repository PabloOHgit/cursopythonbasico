#Ejercicio 3. Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor de ellos.

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if(num1 > num2 and num1 > num3):
    print(num1)
elif(num2 > num1 and num2 > num3):
    print(num2)
else:
    print(num3)