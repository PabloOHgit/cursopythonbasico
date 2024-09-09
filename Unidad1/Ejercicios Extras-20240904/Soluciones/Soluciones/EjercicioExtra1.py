#Ejercicio Extra 1
"""Una panadería vende trozos de tarta a 3.49€ cada una. El trozo que no es el día tiene un descuento del 60%.
 Escribir un programa que comience leyendo el número de trozos vendidos que no son del día. 
 Después el programa debe mostrar el precio habitual de un trozo, el descuento que se le hace por
   no ser fresco y el coste final total."""
trozoFresco = int(input("Introduce el número de trozos vendidos: "))
trozo = int(input("Introduce el número de trozos vendidos que no son frescos: "))
precio = 3.49 
descuento = 0.6
coste = trozoFresco * precio
costeNoFresco = trozo * precio * (1 - descuento)
print("El coste del trozo de tarta fresco es ",precio,"€")
print("El descuento de trozo de tarta de ayer es ",(descuento * 100),"%")
# Utilizamos round(variable,2) para redondear el valor a 2 decimales
print("El total de trozos de hoy es " ,round(coste,2),"€")
print("El total de trozos de ayer es " ,round(costeNoFresco,2),"€")
print("El total es",round(coste+costeNoFresco,2),"€")

