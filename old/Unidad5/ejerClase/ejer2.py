# Ejercicio 2:
# ▰ Crear una clase Ordenador.
# ▰ Declarar una variable estática llamada encendido y asignarle el valor False.
# ▰ En el constructor, le pasamos como argumentos: procesador, memoria,
# Ram y sistemaOperativo (valor booleano).
# ▰ Crear el método __str__ y que muestre todos los datos.
# ▻ Tener en cuenta que sistemaOperativo es booleano, realizar un control
# mediante un if dentro del método. Si tiene sistema operativo que muestre un
# mensaje como que lo tiene además del resto de datos, y si por el contrario no lo
# tiene que diga que no tiene sistema operativo y el resto de los datos.
# ▰ Instanciamos 2 objetos Ordenador diferentes, uno con sistemaOperativo = True y el
# otro con sistemaOperativo = False.
# ▰ Imprimir los 2 objetos instanciados y ver los diferentes mensajes.

class Ordenador:
    encendido = False
    
    def __init__(self,procesador,memoria,Ram,SO=False):
        self.procesador = procesador
        self.memoria = memoria
        self.Ram = Ram
        self.SO = SO
        
    def __str__(self):
        if self.SO:
            return f"El ordenador tiene sistema operativo y {self.procesador},{self.memoria},{self.Ram}"
        else:
            return f"El ordenador NO tiene sistema operativo y {self.procesador},{self.memoria},{self.Ram}"
        
ordenador1 = Ordenador("x8","256 SSD","36G RAM",True)
ordenador2 = Ordenador("x3","128 SSD","14G RAM")
ordenador3 = Ordenador("x1","1024 HDD","8 RAM",True)

ordenadores = [ordenador1,ordenador2,ordenador3]

for ordenador in ordenadores:
    print(ordenador)
    
# print("\n",ordenador1)
# print("\n",ordenador2)
