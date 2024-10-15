# 1. Crear clase Discoteca.
# a. Variables de instancia: Nombre, horario de apertura, código de
# vestimenta (booleano)
# b. Método:
# i. Comprobar si la discoteca esta abierta. Se puede importar
# el módulo para trabajar con fechas.
# ii. Comprobar si la discoteca tiene código de vestimenta.
# c. Instanciar 2 discotecas.
# d. Comprobar si dejarían entrar en sandalias de playa, y bermudas a
# Tom “El guiri” a las 16:00.
# e. Tom sigue sin cambiarse de ropa, pero ahora va a probar a la otra
# discoteca, comprobar si lo dejan pasar

import datetime

class Discoteca:
    
    def __init__(self,nombre,horarioApertura,horarioCierre,codVestimenta=True):
        self.nombre = nombre
        self.horarioApertura = horarioApertura
        self.horarioCierre = horarioCierre
        self.codVestimenta = codVestimenta
        
    def compruebaHorario(self,horario):
        horarioApertura = datetime.datetime.strptime(self.horarioApertura, "%H:%M").time()
        horarioCierre = datetime.datetime.strptime(self.horarioCierre, "%H:%M").time()
        # hora_actual = datetime.datetime.now().time()
        if horarioApertura < horarioCierre:
            if horarioApertura < horario < horarioCierre:
                return True
            else:
                return False
        elif horarioApertura > horarioCierre:
            if horarioCierre < horarioApertura < horario:
                return True
            else:
                return False
        # if horarioApertura < horarioCierre:  # Horario normal
        #     return horarioApertura < hora_actual < horarioCierre
        # else:  # Horario que cruza medianoche
        #     return hora_actual > horarioApertura or hora_actual < horarioCierre
        
    def compruebaVestimenta(self):
        return self.codVestimenta == True        
        
discoteca1 = Discoteca("Chichos","17:00","23:00",False)
discoteca2 = Discoteca("Lolailo","10:00","23:59")
discoteca3 = Discoteca("Afters","00:00","08:00")

# PROBANDO SI LA HORA ACTUAL PERMITE ACCESO EN EL HORARIO DE LA DISCOTECA
# hora_actual = datetime.datetime.now().time()
# print(discoteca3.compruebaHorario(hora_actual))
# print(discoteca2.compruebaVestimenta())

def uso_discoteca(vestimenta,horario,discoteca):
    horario_frmt = datetime.datetime.strptime(horario, "%H:%M").time()
    if vestimenta == discoteca.codVestimenta or (vestimenta == True and discoteca.codVestimenta == False):
    # FORMA PARA DECLARAR VESTIMENTA == FALSE y discoteca.codVestimenta == True (lo declaramos asi por defecto)
    # if vestimenta == discoteca.codVestimenta or (not vestimenta and discoteca.codVestimenta):
        if discoteca.compruebaHorario(horario_frmt):
            return f"Puede acceder a la discoteca {discoteca.nombre} dentro de horario y vestimenta"
        else:
            return f"NO puede acceder a la discoteca {discoteca.nombre} fuera de horario"
    else:
        return f"NO puede acceder a la discoteca {discoteca.nombre}, por no ir bien vestido"

# PROBANDO LA FUNCION MANUALMENTE PARA VALIDAR 
# LOS METODOS DE INSTANCIA DE COMPRUEBA_HORARIO Y COMPRUEBA_VESTIMENTA
# uso_discoteca(False,"16:00",discoteca1)
# uso_discoteca(False,"18:00",discoteca1)
# uso_discoteca(True,"16:00",discoteca1)
# uso_discoteca(True,"18:00",discoteca1)
# uso_discoteca(False,"16:00",discoteca2)
# uso_discoteca(False,"01:00",discoteca3)

vestimenta = False
horario = "12:00"
nombre = ""

nombre = input("¿Cómo se llama la persona que quiere entrar a una de las discotecas?: ")
while True:
    horario = input("¿A qué hora quiere acceder a la discoteca? (ejemplo 20:30): ")
    if horario == "":
        print("No has puesto ninguna hora, repitelo por favor.")
    else:
        break
while True:
    discoteca = input(f"¿A qué discoteca quiere acceder? {discoteca1.nombre},{discoteca2.nombre} o {discoteca3.nombre} (1,2,3): ")
    if discoteca == "1":
        discoteca = discoteca1
        break
    elif discoteca == "2":
        discoteca = discoteca2
        break
    elif discoteca == "3":
        discoteca = discoteca3
        break
    else:
        print("No has elegido una discoteca de las propuestas.")
while True:
    ropa = input("¿Va bien vestid@ o de manera informal (responde 'bien' o ' informal'): ")
    if ropa == "bien":
        vestimenta = True
        break
    elif ropa == "informal":
        vestimenta = False
        break
    else:
        print("No has respondido correctamente a la pregunta.")
         
usodiscoteca = uso_discoteca(vestimenta,horario,discoteca)
print(f"{nombre} {usodiscoteca}")

    
        


