"""Ejercicio 5. Tenemos la pantalla del móvil bloqueada. Partiendo de un
PIN_SECRETO, intentaremos desbloquear la pantalla. Tenemos hasta 3
intentos. Simula el proceso con Python. En caso de acceder, lanza al usuario
'login correcto'. Sino, 'llamando al policía'."""

contraseña = "clave"
pass_usuario = ""

for i in range(3):
    pass_usuario = input("\nIntroduce la clave, tienes 3 intentos: ")
    if(pass_usuario == contraseña):
        print("\nLogin correcto")
        break
    i += 1
if(pass_usuario != contraseña):
    print("\nLlamando a la policía")