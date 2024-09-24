datos_olimpiadas = """Pais;oro;plata;bronce\nEstados Unidos de América;40;44;42\nRepública Popular de China;40;27;24\nJapón;20;12;13"""

# Creamos una lista en datos_olimpicos con 4 trozos al dividir con \n
datos_olimpicos = datos_olimpiadas.split("\n")
# Creamos el diccionario final, vacío, que queremos crear con los datos
medallero_general = {}

# for pais_medallas in datos_olimpicos[1:]:
#     lista_pais_medallas = pais_medallas.split(";")
#     # print(lista_pais_medallas)
#     medallero = {"oro":lista_pais_medallas[1],"plata":lista_pais_medallas[2],"bronce":lista_pais_medallas[3]
#     }
#     medallero_general[lista_pais_medallas[0]] = medallero
# print(medallero_general)

################# OTRA MANERA ############### LA QUE MAS ME GUSTA
    
for pais_medallas in datos_olimpicos[1:]:
    lista_pais_medallas = pais_medallas.split(";")
    medallero_general[lista_pais_medallas[0]] = dict(oro = lista_pais_medallas[1],plata = lista_pais_medallas[2],bronce = lista_pais_medallas[3])

print(medallero_general)

################# OTRA MANERA ###############

# medallero_pais = {}
# lista_informacion_paises = datos_olimpiadas.splitlines()

# datos_medallero = lista_informacion_paises[0].split(";")

# for pais in lista_informacion_paises[1:]:
#     pais,oro,plata,bronce = pais.split(";")
#     medallero_pais[pais] = {datos_medallero[1]:oro,"plata":plata,"bronce":bronce}
# print(medallero_pais)