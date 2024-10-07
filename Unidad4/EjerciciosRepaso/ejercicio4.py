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


# VERSION PARA ELEGIR CUALQUIER MES o CUALQUIER TRIMESTRE
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

meses = list(fiestas.keys())

primer_trimestre = meses[0:3]
segundo_trimestre = meses[3:6]
tercer_trimestre = meses[6:9]
cuarto_trimestre = meses[9:12]

# primer_trimestre = ("enero","febrero","marzo")
# segundo_trimestre = ("abril","mayo","junio")
# tercer_trimestre = ("julio","agosto","septiembre")
# cuarto_trimestre = ("octubre","noviembre","diciembre")

def crea_lista_fiestas(periodo):
    for mes in periodo:
        evento_fiestas = []
        dia_fiestas = []
        for dia,evento in fiestas[mes].items():
            dia_fiestas.append(dia)
            evento_fiestas.append(evento)
        print(f"\nLas fiestas de {mes.upper()} son: ")
        for dia in dia_fiestas:
            print(f"El dia {dia} hay evento {evento_fiestas[dia_fiestas.index(dia)]}")

def crea_mes_fiestas(periodo):
    evento_fiestas = []
    dia_fiestas = []
    for dia,evento in fiestas[periodo].items():
        dia_fiestas.append(dia)
        evento_fiestas.append(evento)
    print(f"\nLas fiestas de {periodo.upper()} son: ")
    for dia in dia_fiestas:
        print(f"El dia {dia} hay evento {evento_fiestas[dia_fiestas.index(dia)]}")

while True:
    periodo = input("\nElige un mes o escribe trimestre para mostrar sus eventos: ").lower()
    if periodo in fiestas:
        crea_mes_fiestas(periodo)
        break
    elif periodo == "trimestre":
        while True:
            periodo = input("\nElige primero, segundo, tercero o cuarto: ").lower()
            if periodo == "primero":
                periodo = primer_trimestre
                break
            elif periodo == "segundo":
                periodo = segundo_trimestre
                break
            elif periodo == "tercero":
                periodo = tercer_trimestre
                break
            elif periodo == "cuarto":
                periodo = cuarto_trimestre
                break
            else:
                # continue
                print("\nVuelve a intentarlo...")
        crea_lista_fiestas(periodo)
        break
    else:
        print("\nPrueba de nuevo...")