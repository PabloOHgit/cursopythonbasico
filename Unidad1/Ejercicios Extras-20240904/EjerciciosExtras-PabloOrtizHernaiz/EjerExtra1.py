#Ejercicios Extras
"""Ejercicio 1: Una panadería vende trozos de tarta a 3.49€ cada una. El trozo que 
no es el día tiene un descuento del 60%.
Escribir un programa que comience leyendo el número de trozos vendidos de 
hoy como que los no son del día. 
Después el programa debe mostrar el precio habitual de un trozo, el descuento 
que se le hace por no ser fresco, el coste de lo ganado en los trozos del día y los 
que no, y el coste final total."""

precio_habitual = 3.49
precio_dto = round(3.49*0.40,2) #multiplicando por 0.40 se hace el 60%
trozos_total = int(input("Cuántos trozos se han cocinado hoy? "))
trozos_hoy = int(input("Cuántos trozos se han vendido hoy? "))
trozos_dto = trozos_total-trozos_hoy
coste_hoy = round(trozos_hoy*precio_habitual,2)
coste_dto = round(trozos_dto*precio_dto,2)

print("El precio habitual de un trozo es",precio_habitual,",el precio con descuento es",precio_dto,
      ", se han vendido hoy",trozos_hoy,"trozos, el total ganado con los trozos de hoy es",coste_hoy,
      ", los trozos que no son de hoy son",trozos_dto,", el coste con dichos trozos es",coste_dto,
      ", el coste total final es",coste_hoy+coste_dto)
