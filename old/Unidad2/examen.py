# cadena_cuenta = input("Introduce un texto para contar cuantas letras tiene: ")
# # El input es: "Hola buenas tardes"
# print(f"El número de letras de la frase introducida es: {len(cadena_cuenta)}")
# # Imprime lo siguiente: "El número de letras de la frase introducida es: 18"


# nombres = ["Ana", "Lucia", "Elena", "Julia", "Clara", "Lucia", "Ana", "Ana", "Maria", "Ana" ] 
# cuenta_anas  = 0
# cuenta_lucias = 0
# cuenta_elenas = 0
# cuenta_claras = 0
# cuenta_julias = 0
# cuenta_marias = 0
# for nombre in nombres:
#     if nombre == "Ana":
#         cuenta_anas += 1
#     elif nombre == "Lucia":
#         cuenta_lucias += 1
#     elif nombre == "Elena":
#         cuenta_elenas += 1
#     elif nombre == "Julia":
#         cuenta_julias += 1
#     elif nombre == "Clara":
#         cuenta_claras += 1
#     elif nombre == "Maria":
#         cuenta_marias += 1
# print(f"Hay {cuenta_anas} Ana")
# print(f"Hay {cuenta_lucias} Lucia")
# print(f"Hay {cuenta_elenas} Elena")
# print(f"Hay {cuenta_julias} Julia")
# print(f"Hay {cuenta_claras} Clara")
# print(f"Hay {cuenta_marias} Maria")
        
# A partir de esta tupla = (8,2), modifica el valor para que sea (9,2). 

# tupla = (8,2)

# lista = list(tupla) # Pasamos la tupla a lista llamándola "lista"
# lista[0] = 9 # Cambiamos el valor "8" de la posición 0 , introduciendo el valor "9" que se solicita

# tupla = tuple(lista) # Pasamos la lista a tupla sobre la misma variable que teníamos de tupla

# print(tupla) # Imprime (9,2)




# A. Crea un diccionario con nombre agenda con el formato Mes { dia: evento} y  que contenga los siguientes datos: (0.5)

# NOTA: El dia se puede poner en la clave tanto como int como string.

#           Enero: 1= Año Nuevo, 31 = Cumpleaños Loreto

#           Febreo: 14 = San Valentin

#           Octubre:  15 = Examen Final Python

#           Diciembre:  24 = Noche Buena ,25= Navidad

# A. Crear agenda
agenda = {
    "Enero":{"1":"Año Nuevo","31":"Cumpleaños Loreto"},
    "Febrero":{"14":"San Valentín"},
    "Octubre":{"15":"Examen Final Python"},
    "Diciembre":{"24":"Noche Buena","25":"Navidad"}
    
}
print(agenda)

# B.  Muestra por pantalla, el evento del día 31 de enero. (0.5)
for mes,evento in agenda.items():
    for dia,eventos in evento.items():
        if "31" in dia:
            print(eventos)
        

# C. Verificar si hay evento en abril en la agenda. (0.5)
for mes,evento in agenda.items():
    if "Abril" in mes:
        print("Hay eventos en el mes de Abril")
    else:
        print("NO hay eventos en el mes de Abril")
        break

# D. Mostrar todo el contenido de diciembre (0.5)
for mes,evento in agenda.items():
    if "Diciembre" in mes:
        print(evento)