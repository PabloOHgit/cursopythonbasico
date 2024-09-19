# Ejercicio 6:
# A. Crea una tupla anidada para representar una pequeña biblioteca.
# Cada elemento de la tupla será un libro con título, autor y año de
# publicación.
# • Cien años de soledad, Gabriel García Márquez, 1967
# • El señor de los anillos, J.R.R. Tolkien, 1954
# • La sombra del viento, Carlos Ruiz Zafón, 2001
# • Orgullo y prejuicio, Jane Austen, 1813
# • 1984, George Orwell, 1949
# • Harry Potter y las Reliquias de la Muerte, J.K. Rowling, 2007
# • Ángeles y demonios, Dan Brown, 2000
# B. Imprime todos los libros publicados después de 2000

biblioteca = (("Cien años de soledad", "Gabriel García Márquez", 1967),("El señor de los anillos", "J.R.R. Tolkien", 1954),("La sombra del viento", "Carlos Ruiz Zafón", 2001),("Orgullo y prejuicio", "Jane Austen", 1813),(1984, "George Orwell", 1949),("Harry Potter y las Reliquias de la Muerte", "J.K. Rowling", 2007),("Ángeles y demonios", "Dan Brown", 2000))
libros_2000 = []
for libro in biblioteca:
    if libro[2] > 2000:
        libros_2000.append(libro)
tupla_2000 = tuple(libros_2000)
for i in tupla_2000:
    print(f"Los libros publicados después del año 2000 son: {i}")
    
#Otro método

# Tupla de biblioteca
biblioteca = (
    ("Cien años de soledad", "Gabriel García Márquez", 1967),
    ("El señor de los anillos", "J.R.R. Tolkien", 1954),
    ("La sombra del viento", "Carlos Ruiz Zafón", 2001),
    ("Orgullo y prejuicio", "Jane Austen", 1813),
    ("1984", "George Orwell", 1949),
    ("Harry Potter y las Reliquias de la Muerte", "J.K. Rowling", 2007),
    ("Ángeles y demonios", "Dan Brown", 2000)
)

# Crear una lista de libros publicados después del año 2000
libros_2000 = [libro for libro in biblioteca if libro[2] > 2000]

# Convertir la lista en una tupla
tupla_2000 = tuple(libros_2000)

# Imprimir los libros publicados después del año 2000
print("Los libros publicados después del año 2000 son:")
for libro in tupla_2000:
    print(libro)

