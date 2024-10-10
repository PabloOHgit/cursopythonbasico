# 4. Crear la clase Autor:
# a. Variables de instancia: Nombre, año de nacimiento.
# b. Instanciar 3 autores.
# Crear la clase Libro.
# c. Variables de instancia: titulo, autor, año de publicación,
# leído=False.
# d. Métodos:
# i. Comprobar si el libro esta leído
# ii. Cambiar el valor a leído del libro.
# e. Instanciar 5 libros y pasarle como parámetro el autor instanciado
# anteriormente.
# f. Llamar a los métodos creados y comprobar su cambio de valor.
# g. Mostrar la información del libro
# h. Crear una lista, almacenar los libros en ella, y tras recorrerla
# mostrar los libros de uno de los autores creados anteriormente.

class Autor:
    
    def __init__(self,nombre,anacimiento):
        self.nombre = nombre
        self.anacimiento = anacimiento

class Libro:
    
    def __init__(self,titulo,autor,apublicación,leido=False):
        self.titulo = titulo
        self.autor = autor
        self.apublicación = apublicación
        
autor1 = Autor("Luis Bili","15-03-1986")
autor2 = Autor("Eva Gloria","4-02-1979")
autor3 = Autor("Alberto Lucho","22-11-1985")