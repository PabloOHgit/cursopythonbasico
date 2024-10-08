# Ejercicio 2:
# ▰ En la clase Ordenador que creamos anteriormente, vamos a añadir 1 método:
# ▻ Método instalarSO: Este método comprueba si el ordenador tiene SO. Si no lo
# tiene, le pregunta al usuario que SO quiere instalar. Y luego muestra el sistema
# operativo instalado. Si tiene SO, le dice al usuario que ya tiene SO.
# ▻ Instanciar un objeto con SO = False. Imprimir el objeto creado.
# ▻ Llamar al método instalarSO e imprimir de nuevo el objeto.


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
        
    def instalarSO(self):
        if self.SO == False:
            sistema = input("¿Qué Sistema Operativo quieres instalar?: ")
            print(f"El sistema operativo instalado es {sistema}")
            self.SO = True #Le cambia el valor del parámetro Sistema Operativo a TRUE al objeto ordenador con el que tratamos
        else:
            print("Ya tiene Sistema Operativo")
        
        
ordenador1 = Ordenador("x8","256 SSD","36G RAM",True)
ordenador2 = Ordenador("x3","128 SSD","14G RAM")
ordenador3 = Ordenador("x1","1024 HDD","8 RAM",True)

print(ordenador2)#No tiene sistema operativo
ordenador2.instalarSO()#Se lo instala
print(ordenador2)#Se verifica que ya lo tiene instalado porque al cambiarlo a TRUE indica que si tiene SO

