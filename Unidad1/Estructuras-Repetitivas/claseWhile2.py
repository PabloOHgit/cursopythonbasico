#2. Calcular el factorial de un número

factorial_usuario = int(input("Introduce un número para calcular su factorial "))
factorial = factorial_usuario
total = factorial

while(factorial > 1):
    factorial -= 1
    total *= factorial
else:
    print("El factorial de",factorial_usuario,"es",total)
    
