#1. Ejercicios de Estructuras condicionales
"""Ejercicio 1: Escribir un programa que almacene la cadena de caracteres
password en una variable, pregunte al usuario por la contraseña e imprima por
pantalla si la contraseña introducida por el usuario coincide con la guardada en
la variable."""

password = "clave"
pregunta_pass = input("Escribe la contraseña: ")

if(password == pregunta_pass):
    print("La contraseña introducida es correcta")
else:
    print("La contraseña no coincide, sigue probando")
