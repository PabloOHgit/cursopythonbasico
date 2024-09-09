"""Ejercicio 3. Escriba un programa que pida el año actual y un año cualquiera y
que escriba cuántos años han pasado desde ese año o cuántos años faltan para
llegar a ese año."""

a_actual = input("Introduce el año actual ")

a_cualquiera = input("Introduce un año cualquiera ")

comprobacion_anios = int(a_actual)-int(a_cualquiera) 

if(a_actual > a_cualquiera):
    print("Han pasado",comprobacion_anios,"años hasta la fecha actual")
else:
    print("Faltan",abs(comprobacion_anios),"años hasta la fecha introducida")