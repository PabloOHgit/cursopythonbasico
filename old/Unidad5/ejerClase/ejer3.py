# Ejercicio 1:
# ▰ En la clase Perro que creamos anteriormente, vamos a añadir 2 métodos:
# ▻ Método ladrar: Que muestre el nombre del perro y un mensaje que ponga esta
# ladrando.
# ▻ Método jugar: se le pasa por parámetro pelota que es de tipo booleano.
# ▻ Si pelota == True. Nombre del perro esta jugando con su pelota
# ▻ Si pelota == False. Nombre del perro esta jugando.

class Perro:
    contador_perros = 0
    
    def __init__(self,nombre,raza,edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        Perro.contador_perros += 1
        
    def __str__(self):
        return f"El nombre del perro es {self.nombre} y la raza es {self.raza}"
    
    def ladrar(self):
        # print(f"{self.nombre} está ladrando")
        return f"{self.nombre} está ladrando"
    
    def jugar(self,pelota=True):
        if pelota:
            # print(f"{self.nombre} está jugando con su pelota")
            return f"{self.nombre} está jugando con su pelota" 
        else:
            # print(f"{self.nombre} está jugando...")
            return f"{self.nombre} está jugando..."

perro1 = Perro("Jara","Collie",3)
perro2 = Perro("Grey","Braco",2)
perro3 = Perro("Lisa","Mezclete",5)

print(perro1.ladrar())
# perro1.ladrar()
print(perro2.jugar(False))
# perro2.jugar(False)
print(perro3.jugar())
# perro3.jugar()