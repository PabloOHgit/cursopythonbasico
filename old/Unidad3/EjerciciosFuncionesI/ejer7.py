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


def pedir_nombre():
    # global pide_nombre - NO HACE FALTA GLOBALIZARLA PUES PUEDO LLAMAR A LA FUNCION DENTRO DE LA OTRA OBTENIENDO EL VALOR DE LA VARIABLE
    pide_nombre = ""
    while True:
        if pide_nombre == "":
            pide_nombre = input("Introduce tu nombre y apellidos: ").title()
        else:
            break
    return pide_nombre

def cuenta_letras(apellido):
    nombre_apellidos = apellido.split(" ")
    apellido = nombre_apellidos[1]
    apellido_identificador = [letra for letra in nombre_apellidos[1]]
    cuenta_apellido = len(apellido_identificador)
    nombre_apellido = nombre_apellidos[0]

    return str(cuenta_apellido),nombre_apellido

def introducir_dni():
    dni = ""
    while True:
        if len(dni) < 3:
            dni = input("Introduce DNI: ")
        else:
            break
    corta_dni = dni[:3]
    return str(corta_dni)
            

# DESEMPAQUETO LA TUPLA QUE GENERA LA FUNCION CON EL RETURN DE DOS VARIABLES, EN DOS VARIABLES PARA PODER USARLAS, LAS PONE EN ORDEN
cuenta_apellido,nombre_apellido = cuenta_letras(pedir_nombre())
corta_dni = introducir_dni()

identificador = nombre_apellido+cuenta_apellido+corta_dni

print(f"Tu identificador único es: {identificador}, se compone de nombre: {nombre_apellido}, la cantidad de letras del primer apellido: {cuenta_apellido} y de los primeros 3 dígitos de tu DNI: {corta_dni}")