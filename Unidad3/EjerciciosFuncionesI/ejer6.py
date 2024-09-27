# 6. Crear un programa que le diga al usuario que ingrese un número entero
# e informar si es primo o no.

def num_primo(num):
    if num < 2:
        return False
    for i in range(2,num): 
        if num % i == 0:
            return False
    return True
        
while True:
    numero = int(input("\nIntroduce un número entero para calcular si es primo, '0' para SALIR: "))
    if numero > 0:
        if num_primo(numero):
            print("\nEl número introducido es primo")
        else:
            print("\nEl número introducido NO es primo")
    else:
        break



