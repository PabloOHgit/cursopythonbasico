libros = [("Orgullo y prejuicio",1813),
          ("Harry Potter y la piedra filosofal",1840),#cambiarle la fecha
          ("El mando mágico",1840)]#cambiarle el nombre a "caldero" en vez de "mando"

for libro in libros:
    if libro[0] == "Harry Potter y la piedra filosofal":
        lista = list(libro)
        lista[1] = 1997
        librot = tuple(lista)
        libros[1] = librot
    elif libro[0] == "El mando mágico":
        lista = list(libro)
        lista[0] = "El caldero mágico"
        libroa = tuple(lista)
        libros[2] = libroa
        
        
print(libros)
            
    