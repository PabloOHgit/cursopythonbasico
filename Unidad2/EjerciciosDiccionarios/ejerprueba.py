persona = {"nombre":"Loreto","edad":"32"}
# Cambiar valor
persona["edad"] = 25
# Añadir
persona["profesion"] = ["Informática"]
# Borrar
del persona["profesion"]

for clave,valor in persona.items():
    print(clave,valor)