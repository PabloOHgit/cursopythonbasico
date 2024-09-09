#Vamos a realizar un ejercicio de mostrar la serie de fibonacci hasta el número que elija el usuario
print("Ejercicio de serie de Fibonacci\n")
numero = int(input("Elige un número de la serie de Fibonacci para mostrar todos hasta ese número: \n"))

num1 = 0
num2 = 1
suma = 0

print("\nLa serie de Fibonacci elegida es la siguiente:\n")
while(suma <= numero):
        num1 = num2
        num2 = suma
        #suma = num1 + num2      
        if(suma == numero):
            print(suma)
            print("\nLa serie ha finalizado")
        else:
            print(suma, end=", ")
        suma = num1 + num2  
        