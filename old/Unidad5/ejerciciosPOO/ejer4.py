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
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Año nacimiento: {self.anacimiento}"

class Libro:
    
    def __init__(self,titulo,autor,apublicación,leido=False):
        self.titulo = titulo
        self.autor = autor
        self.apublicación = apublicación
        self.leido = leido
        
    def comprobar_leido(self):
        if self.leido == True:
            return f"El libro '{self.titulo}' está leído"
        else:
            return f"El libro '{self.titulo}' no está leído"
        
    def libro_leido(self):
        self.leido = True
        
    def __str__(self):
        if self.leido == True:
            leido = "Libro leído"
        else:
            leido = "Libro no leído"
        return f"{self.titulo},{self.autor},{self.apublicación},{leido}"
            
        
autor1 = Autor("Luis Bili","15-03-1986")
autor2 = Autor("Eva Gloria","4-02-1979")
autor3 = Autor("Alberto Lucho","22-11-1985")

libro1 = Libro("Programa en Python","Loretix","2024",True)
libro2 = Libro("Pesadillas con Python","Ambrosius","2022")
libro3 = Libro("Muere con Java",autor1,"2023",True)
libro4 = Libro("Estudia como nunca",autor2,"2023")
libro5 = Libro("Aprende mucho",autor3,"2023",True)

print(libro1.comprobar_leido())
print(libro2.comprobar_leido())
# libro2.libro_leido()
# print(libro2.comprobar_leido())
print(libro3)

lista_libros = [libro1,libro2,libro3,libro4,libro5]

for libro in lista_libros:
    if libro.autor == autor2:
        print(libro)