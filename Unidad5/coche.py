class Motor:     
    def __init__(self,potencia,cilindrada):
        self.potencia = potencia
        self.cilindrada = cilindrada
        
    def __str__(self):
        return f"El motor tiene potencia {self.potencia} cv y cilindrada {self.cilindrada} cc"

class Coche:
    # encendido = False
    num_coches = 0
    
    def __init__(self,marca,modelo,color,motor,puertas=5):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.puertas = puertas
        self.motor = motor
        Coche.num_coches += 1
    
    def __str__(self):
        return f"El coche es {self.marca} y modelo {self.modelo}, potencia {self.motor.potencia}"
        

print(Coche.num_coches)

motor1 = Motor(130,1500)
motor2 = Motor(180,2000)

coche1 = Coche("Audi","Q3","Gris",motor1)
coche2 = Coche("Audi","Q5","Gris",motor2)
print(Coche.num_coches) 

print(coche1)

print(coche2)




