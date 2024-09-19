cartelera = [
    ("Forrest Gump","ficcion",142),
    ("Joker","drama",132),
    ("Gladiator II","accion",125),
    ("Dune","ficcion",166),
    ("Furiosa","aventuras",138)
    ]

# genero_input = input("Elige género para la búsqueda (ficcion,accion,drama,aventuras): ")
# for genero in cartelera:
#     if genero[1] == genero_input:
#         print(f"La película es, título: {genero[0]}, género: {genero[1]}, duración: {genero[2]}.")
        
while True:
    menu = int(input("Introduce la opción que desees (1-5): "))
    if menu == 1:
        titulo_input = input("Elige la película a buscar por título: ")
        while True:            
            for titulo in cartelera: 
                if titulo[0] == titulo_input:
                    print(f"La película es, título: {titulo[0]}, género: {titulo[1]}, duración: {titulo[2]}.")
                    break
            # if titulo[0] != titulo_input:
            #     titulo_input = input("No existe esa película, pruebe de nuevo o escriba SALIR: ")
            # if titulo_input == "salir":
            #     print("Saliendo...")
            #     break
    break
            
listado_contraseñas = [("user1","pass1"),("user2","pass2"),("admin","admin_pass")]

for usuario in listado_contraseñas:
    