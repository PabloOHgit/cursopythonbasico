# Ejercicio 2. Ingresar un mail por teclado. Verificar si el texto ingresado contiene solo un
# carácter "@".

email = input("Introduce un email: ")

cuenta = email.count("@")
if cuenta == 1:
    print("El email contiene una @ y es correcto.")
else:
    print("El email contiene más de una @ y no es correcto.")