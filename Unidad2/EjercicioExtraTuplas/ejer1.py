# LORETIX
# Crear un programa para gestionar la plataforma de video LORETIX.
# A. Crear una lista de usuarios con sus contraseñas para poder acceder a la
# plataforma, y una para el administrador. (Lista con tuplas anidadas)
# a. El usuario tendrá acceso a unas opciones, mientras que el
# administrador a otras.
# B. Crear una lista de películas: Define una lista llamada cartelera y agrega
# al menos 5 películas diferentes. Por ejemplo: Nombre, genero, duración.
# C. Menú con las diferentes opciones.
# Usuario:
# A. Buscar película por título.
# B. Buscar películas por género.
# C. Cambiar contraseña de usuario
# D. Crear listas de películas favoritas que se quiere ver.
# E. Mostrar la lista de películas favoritas.
# Administrador:
# A. Agregar una nueva película.
# B. Modificar el contenido de la lista de películas.
# C. Eliminar una película de la lista.

listado_contraseñas = [
    ("user1","pass1"),
    ("user2","pass2"),
    ("admin","admin_pass")
    ]

lista_contraseñas_tupla = tuple(listado_contraseñas)

cartelera = [
    ["Forrest Gump","ficcion",142],
    ["Joker","drama",132],
    ["Gladiator II","accion",125],
    ["Dune","ficcion",166],
    ["Furiosa","aventuras",138]
    ]
usuario = ""
contraseña = ""

print("------LORETIX------"
      "\n"
      "Plataforma de vídeo")

user_normal = False
user_admin = False

while True:
    usuario = input(f"Introduce tu usuario: ")
    contraseña = input(f"Introduce tu contraseña: ")
    
    if usuario == "admin" and contraseña == "admin_pass":
        print("Es correcto, eres el administrador")
        user_admin = True
        break
    elif usuario == "user1" and contraseña == "pass1":
        print("Es correcto, eres un usuario normal")
        user_normal = True
        break
    elif usuario == "user2" and contraseña == "pass2":
        print("Es correcto, eres un usuario normal")
        user_normal = True
        break
    else:
        print("Usuario y/o contraseña incorrectas, repita de nuevo")
        
if user_normal == True:
    print("\nMenú usuario normal:"
          "\n1. Buscar película por título"
          "\n2. Buscar película por género"
          "\n3. Cambiar contraseña de usuario"
          "\n4. Crear lista de películas favoritas"
          "\n5. Mostrar la lista de películas favoritas")
    
while True:
    menu = int(input("Introduce la opción que desees (1-5): "))
    if menu == 1:
        titulo_input = input("Elige la película a buscar por título: ")
        for titulo in cartelera:
            if titulo[1] == titulo_input:
                print(f"La película es, título: {titulo[0]}, género: {titulo[1]}, duración: {titulo[2]}.")

# for usuario in listado_contraseñas:
#     if (usuario[0] == "admin" and usuario[1] == "admin_pass"):
#         print("Es correcto, eres el administrador")
#     else:
#         print("Es correcto, eres un usuario normal")


