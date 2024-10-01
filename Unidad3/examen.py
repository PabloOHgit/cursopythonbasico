# Crea un programa utlizando funciones para buscar un elemento cualquiera de un diccionario.

# diccionario = {"bolso":"negro", "mando": "blanco","boligrafo":"azul","libreta":"roja"}

# def buscar_elemento(elemento):
#     print(diccionario[elemento])
        
# elemento = input("Introduce el elemento a buscar (bolso, mando, boligrafo, libreta): ")
# print(f"El valor de la clave {elemento} es: ")
# buscar_elemento(elemento)

# Crear un programa con funciones que al introducir una cadena,
# esta la convierta en mayúsculas y separe las palabras por sus espacios.

# def funcion_cadena(cadena):
#     cadena_mayusculas = cadena.upper()
#     cadena_separa = cadena_mayusculas.split(" ")
#     print(cadena_separa)
    
# cadena = input("Introduce un texto para transformarlo: ")
# funcion_cadena(cadena)

# Crear un programa con funciones que cree una clave
# de usuario con las siguientes indicaciones:

# A.  El usuario debe introducir un correo por teclado,
# y hay que separar la parte del nombre de usuario, es decir,
# la parte de la izquierda del @. Por ejemplo: loreto@gmail.com,
# nos quedaríamos solo con loreto. (1 punto)

# B. El usuario debe introducir su día de nacimiento. (1 punto)

# C. Y como resultado debe devolver la unión del nombre,
# el día de nacimiento con el dominio de @altavoces.es
# Resultado: loreto31@altavoces.es (1 punto)

correo = input("Introduce tu dirección de e-mail: ")
fecha = input("Introduce tu fecha de nacimiento formato españa (12 abril 1992): ")

def valida_correo(correo):
    posicion_arroba = correo.find("@")
    nombre_correo = correo[:correo.find("@")]
    return nombre_correo

def valida_fecha(fecha):
    dias_fecha = fecha[:2]
    return dias_fecha
    
def crear_clave_usuario():
    dominio = "@altavoces.es"
    print(valida_correo(correo)+valida_fecha(fecha)+dominio)
    
crear_clave_usuario()