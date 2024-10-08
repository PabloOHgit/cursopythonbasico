#Ejercicio 5: Tenemos la pantalla del móvil bloqueada. Partiendo de un
#PIN_SECRETO, intentaremos desbloquear la pantalla. Tenemos hasta 3
#intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario
#'login correcto'. Sino, 'llamando al policía'.

pin_secreto = 123
print("\nVamos a realizar un ejercicio de adivinar un pin secreto numérico"
      " de 3 cifras, y tenemos 3 intentos")
contador = 0

while(contador < 3):
    clave_user = int(input("\nIntroduce un número entero de 3 cifras por favor "))
    if(clave_user == pin_secreto):
        print("\Login correcto.")
        break
    contador += 1
else: 
    print("\Llamando a la policía")