"""Ejercicio 4. Crea un programa para calcular la superficie y el volumen de una
esfera, dado su radio."""

#a) superficie = 4 * PI * radio al cuadrado
#b) volumen = 4/3 * PI* radio al cubo

radio = int(input("Escribe el valor del radio de la esfera para calcular su superficie y volumen: "))
PI = 3.1416
superficie = 4*PI*radio
volumen = 4/3*PI*radio**2
print("El valor de la superficie de la esfera es:",superficie,"y el valor del volumen es:",volumen)

