#Ejercicio 2. Se ingresan por teclado tres números, si alguno de los valores ingresados es menor a
#10, imprimir en pantalla la leyenda "Algún número es menor a diez".

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if(num1 < 10 or num2 < 10 or num3 < 10):
    print("Algún número es menor a diez")