class Coche:
    # encendido = False
    num_coches = 0
    
    def __init__(self,marca,modelo,color,puertas=5):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.puertas = puertas
        Coche.num_coches += 1
    
    def __str__(self):
        return f"El coche es {self.marca} y modelo {self.modelo}"
        

print(Coche.num_coches)    
coche1 = Coche("Audi","Q3","Gris")
coche2 = Coche("Audi","Q5","Gris",3)
print(Coche.num_coches) 

print(coche1.puertas,coche1.marca)

print(coche1)




