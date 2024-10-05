# Ejercicio 4.
# A partir del siguiente diccionario:
# fiestas = {"enero":{1:"Año Nuevo", 6:"Reyes",31:"Cumpleaños Loreto"},
#  "febrero": {14: "San Valentin"},
#  "marzo": {19: "San José"},
#  "abril":{17: "Jueves Santo",18:"Viernes Santo"},
#  "mayo":{4:"Día de la madre"},
#  "junio":{9: "Día de la Región de Murcia"},
#  "julio":{6:"San Fermín"},
#  "agosto":{15:"Asunción de la Virgen"},
#  "septiembre":{16:"Romeria de la Fuensanta"},
#  "octubre":{12:"El día del Pilar"},
#  "noviembre":{1: "Día de todos los santos"},
#  "diciembre":{6:"Día de la Constitución",8:"Día de la Inmaculada
# Concepción",24:"NocheBuena",25:"Navidad"}}
# A. Sacar las fiestas del primer trimestre, almacenarlas en una lista y mostrarlas.
# B. Imprime las fiestas de diciembre

fiestas = {
    "enero":{1:"Año Nuevo", 6:"Reyes",31:"Cumpleaños Loreto"},
    "febrero": {14: "San Valentin"},
    "marzo": {19: "San José"},
    "abril":{17: "Jueves Santo",18:"Viernes Santo"},
    "mayo":{4:"Día de la madre"},
    "junio":{9: "Día de la Región de Murcia"},
    "julio":{6:"San Fermín"},
    "agosto":{15:"Asunción de la Virgen"},
    "septiembre":{16:"Romeria de la Fuensanta"},
    "octubre":{12:"El día del Pilar"},
    "noviembre":{1: "Día de todos los santos"},
    "diciembre":{6:"Día de la Constitución",8:"Día de la Inmaculada Concepción",24:"NocheBuena",25:"Navidad"}
    }

primer_trimestre = ("enero","febrero","marzo")
segundo_trimestre = ("abril","mayo","junio")
tercer_trimestre = ("julio","agosto","septiembre")
cuarto_trimestre = ("octubre","noviembre","diciembre")


def crea_lista_fiestas(periodo):
    lista_fiestas = []
    for mes,fiesta in periodo.items():
        lista_fiestas.append(mes,fiesta)
    return lista_fiestas

# mes = fiestas["diciembre"]

lista_fiestas = []
for mes,fiesta in fiestas.items():
    lista_fiestas.append([mes,fiesta])

print("diciembre" in lista_fiestas)

# print(crea_lista_fiestas(fiestas))