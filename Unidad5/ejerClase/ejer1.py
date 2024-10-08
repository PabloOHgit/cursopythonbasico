# Ejercicio 1:
# ▰ Crear una clase Perro.
# ▰ Declarar una variable estática llamada contador_perros y asignarle el valor 0.
# ▰ En el constructor, le pasamos como argumentos: nombre, raza y edad.
# ▻ Dentro del constructor llamamos a la variable estática contador_perros y le
# decimos que cuando creemos un nuevo objeto, se le sume 1 a ese contador.
# ▰ Crear el método __str__, y que muestre nombre y raza.
# ▰ Instanciamos 3 objetos Perro diferentes.
# ▰ Imprimimos la llamada a contador_perros. El resultado debe de ser 3.
# ▰ Imprimir uno de los objetos Perro.

class Perro:
    contador_perros = 0
    
    def __init__(self,nombre,raza,edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        Perro.contador_perros += 1
        
    def __str__(self):
        return f"El nombre del perro es {self.nombre} y la raza es {self.raza}"
    
perro1 = Perro("Jara","Collie",3)
perro2 = Perro("Grey","Braco",2)
perro3 = Perro("Lisa","Mezclete",5)

print(Perro.contador_perros)

print(perro2)
    
