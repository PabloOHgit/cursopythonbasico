
contraseñas = [("user1","pass1"),("user2","pass2"),("admin","admin_pass")]

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
        print(f"\nLa contraseña ha sido cambiada satisfactoriamente, es la siguiente: '{tupla_nueva[1]}' para el usuario: '{tupla_nueva[0]}'")
        break
    else:
        salir = input("\nEl usuario/contraseña introducidos no son válidos, prueba de nuevo, o escribe 'salir'.\n").lower()
    if salir == "salir":
        print("\nSaliendo...")
        break
        
print(contraseñas)