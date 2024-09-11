#Ejercicio 4: Escribir un programa que pregunte el correo electrónico del usuario en la
#consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte
#delante de la arroba @) pero con dominio avanza.es.

correo = input("Introduce un correo electronico: ")
arroba = correo.find("@")
dominio = "avanza.es"
correo_nuevo = correo[:arroba+1]+dominio
print(f"El correo con el dominio cambiado es: {correo_nuevo}")