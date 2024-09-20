cartelera = [
    ("Forrest Gump","ficcion",142),
    ("Joker","drama",132),
    ("Gladiator II","accion",125),
    ("Dune","ficcion",166),
    ("Furiosa","aventuras",138)
    ]

contraseñas = [("user1","pass1"),("user2","pass2"),("admin","admin_pass")]


        
while True:
    print("\nMenú usuario normal:"
          "\n1. Buscar película por título"
          "\n2. Buscar película por género"
          "\n3. Cambiar contraseña de usuario"
          "\n4. Crear lista de películas favoritas"
          "\n5. Mostrar la lista de películas favoritas")
    menu = int(input("\nIntroduce la opción que desees (1-5): "))
    if menu == 1:
        print("\nHas elegido '1. Buscar película por título'.")
        titulo_input = input("\nElige la película a buscar por título: ").title()
        while True:                
            verifica_pelicula = False
            print("\n")
            for titulo in cartelera: 
                if titulo[0] == titulo_input:
                    print(f"La película es, título: {titulo[0]}, género: {titulo[1]}, duración: {titulo[2]}.")
                    verifica_pelicula = True
            if verifica_pelicula == False:
                titulo_input = input(f"La película que buscas no existe en nuestra plataforma, prueba de nuevo o pulsa 'salir': ").title()
            if titulo_input == "Salir":
                print("\nSaliendo...")
                break
            if verifica_pelicula == True:
                break
    if menu == 2:
        print("\nHas elegido '2. Buscar película por género'.")
        genero_input = input("\nElige género para la búsqueda (ficcion,accion,drama,aventuras): ").lower()
        while True:                
            verifica_pelicula = False
            print("\n")
            for genero in cartelera:                    
                if genero[1] == genero_input:
                    print(f"Tenemos la siguiente película con ese género, título: {genero[0]}, género: {genero[1]}, duración: {genero[2]}.")
                    verifica_pelicula = True
            if verifica_pelicula == False:
                genero_input = input(f"No hay ninguna película con ese género en nuestra plataforma, prueba de nuevo o pulsa 'salir': ").lower()
            if genero_input == "salir":
                print("\nSaliendo...")
                break
            if verifica_pelicula == True:
                break
    if menu == 3:
            print("\nHas elegido: '3. Cambiar contraseña de usuario'.")
            while True:
                cambia_pass = False
                index_tupla = 0
                usuario = input(f"\nIntroduce tu usuario: ")
                contraseña = input(f"Introduce tu contraseña: ")
                for login in contraseñas:
                    if login[0] == usuario and login[1] == contraseña:
                        tupla_lista = list(login)
                        tupla_lista[1] = input("\nEscribe la nueva contraseña: ")
                        tupla_nueva = tuple(tupla_lista)
                        contraseñas[index_tupla] = tupla_nueva
                        cambia_pass = True
                    index_tupla += 1
                if cambia_pass == True:
                    print("\n************** La contraseña ha sido cambiada satisfactoriamente **************")
                    break
                else:
                    salir = input("\nEl usuario/contraseña introducidos no son válidos, prueba de nuevo, o escribe 'salir'.\n").lower()
                if salir == "salir":
                    print("\nSaliendo...")
                    break
            
# listado_contraseñas = [("user1","pass1"),("user2","pass2"),("admin","admin_pass")]

# for usuario in listado_contraseñas:
    