contador = 0

def autentificacion_correcta(usuario,contra):
    usuarios = {"user":"pass","user1":"1234"}
    if usuario in usuarios and usuarios[usuario] == contra:
        return True
    else:
        return False

# autentificacion_correcta("user","pass")

def iniciar_sesion(usuario,contra):
    global contador
    while contador < 3:        
        if autentificacion_correcta(usuario,contra) == True:
            print("Bienvenido")
            break
        else:
            print("No eres bienvenido aquí")
            usuario = input("Introduce tu usuario: ")
            contra = input("Introduce tu contraseña: ")
        
user = input("Introduce tu usuario: ")
password = input("Introduce tu contraseña: ")
iniciar_sesion(user,password)



#### CON CHAT GPT ###

# # Diccionario con usuarios y contraseñas
# contraseñas = {
#     "user1": 1234,
#     "user2": 5678,
#     "user3": 91011
# }

# # Número máximo de intentos permitidos
# intentos_max = 3
# intentos = 0

# while intentos < intentos_max:
#     # Solicitar nombre de usuario y contraseña por input
#     usuario = input("Introduce tu nombre de usuario: ")
#     contraseña = int(input("Introduce tu contraseña: "))

#     # Comprobar si el usuario existe en el diccionario
#     if usuario in contraseñas:
#         # Comprobar si la contraseña es correcta
#         if contraseñas[usuario] == contraseña:
#             print("¡Acceso concedido!")
#             break  # Salir del bucle si es correcto
#         else:
#             print("Contraseña incorrecta.")
#     else:
#         print("Usuario no encontrado.")
    
#     intentos += 1

#     if intentos < intentos_max:
#         print(f"Te quedan {intentos_max - intentos} intentos.")
#     else:
#         print("Has agotado todos tus intentos.")


