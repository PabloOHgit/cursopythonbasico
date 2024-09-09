#Ejercicio 1: Escribir un programa que muestre todo lo que el usuario introduzca
#hasta que el usuario escriba “salir” que saldrá del programa.

string_user = ""
exit = "salir"

while(string_user != exit):
    string_user = input("\nIntroduce una palabra o texto cualquiera: ")
    print("Lo que has introducido es:",string_user)
if(string_user == exit):
    print("\nHemos acabado, has escrito la palabra 'salir'.")
