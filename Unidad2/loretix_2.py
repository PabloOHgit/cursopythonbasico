contraseñas_lista = [["user1","pass1"],["user2","pass2"],["admin","admin_pass"]]
contraseñas_tupla = [("user1","pass1"),("user2","pass2"),("admin","admin_pass")]

usuario = input(f"Introduce tu usuario: ")
contraseña = input(f"Introduce tu contraseña: ")

contraseñas_lista_1 = list(contraseñas_tupla)

for login in contraseñas_lista_1:
    if login[0] == usuario and login[1] == contraseña:
        listita=list(login)
        listita[1] = input("escribe la nueva contraseña: ")
        tuplita = tuple(listita)
        contraseñas_lista_1[0] = tuplita
        
 
contraseñas_tupla_1 = tuple(contraseñas_lista_1)

print(contraseñas_lista_1)
print(contraseñas_tupla_1)