# 2. Crear clase Cultivo.
# a. Variables de instancia: nombre, variedad, fecha de siembra, fecha
# esperada de cosecha y estado de cosecha = “No iniciado”.
# b. Métodos:
# i. Iniciar cosecha. Se muestra la cosecha que esta en curso y
# se cambia el valor de la variable estado de cosecha a En
# curso.
# ii. Finalizar cosecha. Se muestra que cosecha ha finalizado y
# se cambia el valor de la variable estado de cosecha a
# Finalizado.
# iii. Calcular días restantes para la cosecha, desde la fecha de
# hoy a la fecha estimada de cosecha. Importar el módulo para
# trabajar con fechas.
# c. Crear diferentes cultivos, y utilizar los métodos para cambiar el
# estado de cosecha.
# d. Crear una lista para almacenar los cultivos.
# e. Mostrar la información de los cultivos. (nombre y estado de la
# cosecha)

import datetime

class Cultivo:

    def __init__(self,nombre,variedad,fsiembra,fcosecha,estado="No iniciado"):
        self.nombre = nombre
        self.variedad = variedad
        self.fsiembra = fsiembra
        self.fcosecha = fcosecha
        self.estado = estado

    def iniciarCosecha(self):
        self.estado = "En curso"

    def finalizarCosecha(self):
        self.estado = "Finalizado"

    def calcularDiasCosecha(self,fecha):
        fcosecha_str = datetime.datetime.strptime(self.fcosecha, "%d-%m-%Y")
        fecha_str = datetime.datetime.strptime(fecha, "%d-%m-%Y")

        return f"Faltan {(fcosecha_str - fecha_str).days} días para la cosecha de {self.nombre} {self.variedad}."
        # return (fcosecha_str - fecha_str) #SI DEJO ESTO DARA TAMBIEN HORAS Y NO INTERESA, SOLO QUEREMOS DIAS, ES MAS LIMPIO


    def __str__(self):
        return f"El cultivo de {self.nombre} se encuentra en estado: {self.estado}"

pimientos = Cultivo("Pimiento","Italiano","10-06-2024","25-11-2024","Iniciado")
patatas = Cultivo("Patata","Gallega","2-03-2024","30-12-2024","Iniciado")
tomates = Cultivo("Tomate","Raff","24-9-2024","25-10-2024","Iniciado")

print(pimientos)
pimientos.iniciarCosecha()
print(pimientos)
pimientos.finalizarCosecha()
print(pimientos)

hoy = "10-10-2024"

resultado = pimientos.calcularDiasCosecha(hoy)
resultado1 = patatas.calcularDiasCosecha(hoy)
resultado2 = tomates.calcularDiasCosecha(hoy)
print(resultado)
print(resultado1)
print(resultado2)

cultivos = (pimientos,patatas,tomates)
for cultivo in cultivos:
    print(cultivo)

