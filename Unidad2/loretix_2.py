contraseñas = [["user1","pass1"],["user2","pass2"],["admin","admin_pass"]]

usuario = input(f"Introduce tu usuario: ")
contraseña = input(f"Introduce tu contraseña: ")

for login in contraseñas:
    if login[0] == usuario and login[1] == contraseña:
        login[1] = input("escribe la nueva contraseña: ")
        
contraseñas_tupla = tuple(contraseñas)

print(contraseñas)
print(contraseñas_tupla)