# 6. Crear un programa que le diga al usuario que ingrese un número entero
# e informar si es primo o no.

"""def num_primo(num):
    if num % 2 == 0:
        print("El número introducido NO es primo")
    else:
        print("El número introducido es primo")
        
numero = int(input("Introduce un número entero: "))
num_primo(numero)"""

#### OTRO METODO ##########

def num_primo(num):
    if num % 2 == 0:
        return False
    else:
        return True
        
numero = int(input("Introduce un número entero: "))
if num_primo(numero):
    print("El número introducido es primo")
else:
    print("El número introducido NO es primo")
    