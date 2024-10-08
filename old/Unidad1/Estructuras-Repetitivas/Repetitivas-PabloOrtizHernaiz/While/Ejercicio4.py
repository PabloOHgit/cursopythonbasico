#Ejercicio 4: Crear un programa, que pida al usuario un número, y muestre por
#pantalla, los números en orden inverso hasta 0.

print("\nVamos a realizar un ejercicio en el que vas a introducir un número"
      " y se va a mostrar en pantalla los números hasta 0 en orden inverso")
num = int(input("\nIntroduce el número por favor "))

while(num >= 0):
    if(num == 0):
        print(num)
    else:
        print(num, end=", ")
    num -= 1
else:
    print("\Hemos terminado el ejercicio")
    