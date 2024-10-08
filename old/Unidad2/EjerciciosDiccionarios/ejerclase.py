anidado1 = {"a":1, "b":2}
anidado2 = {"a":1, "b":2}
dueños = {"mama":"Loreto","papa":"Manuel"}

d = {
    "anidado1" : anidado1,
    "anidado2" : anidado2,
    "perro":{"nombre":"Luna","Edad":2,"dueños":dueños}
}

# print(d)

# print(d["perro"]["dueños"]["mama"])

# for due,nombre in dueños.items():
#     print(due,nombre)
    
# for due,nombre in dueños.items():
#     if nombre == "Loreto":
#         print(nombre)

for clave,valor in d.items():
    if clave == "perro":
        for clave1,valor1 in valor.items():
            if clave1 == "dueños":
                for clave2,valor2 in valor1.items():
                    if clave2 == "mama":
                        print(valor2)