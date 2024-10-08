# 7. Crear un programa que pidiendo al usuario su nombre completo y su dni
# con letra, cree un identificador para cada usuario.
# a. Controlar que usuario no introduce el nombre vacío.
# b. Se puede controlar que dni sea correcto
# c. Por cada socio se debe imprimir su identificador único, el cual
# estará formado por: el primer nombre, la cantidad de letras del
# primer apellido y los primeros 3 dígitos de su DNI. Ejemplo:
# Nombre: Loreto Pelegrín Castillo
# DNI: 11111111H
# Loreto8111


# while True:
#     if pide_nombre == "":
#         pide_nombre = input("Introduce tu nombre y apellidos: ").title()
#     else:
#         break

# nombre_apellidos = pide_nombre.split(" ")
# apellido = nombre_apellidos[1]
# apellido_identificador = [letra for letra in nombre_apellidos[1]]
# cuenta_apellido = len(apellido_identificador)

# dni = input("Introduce DNI: ")
# corta_dni = dni[:3]

# identificador = nombre_apellidos[0]+str(cuenta_apellido)+str(corta_dni)
# print(identificador)

def pedir_nombre():
    global pide_nombre
    pide_nombre = ""
    while True:
        if pide_nombre == "":
            pide_nombre = input("Introduce tu nombre y apellidos: ").title()
        else:
            break
        
pedir_nombre()
print(pide_nombre)