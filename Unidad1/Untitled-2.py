
salir = 3
eleccion_user = 0

while(eleccion_user != 3):
    print("1. Comenzar programa")
    print("2. Imprimir números")
    print("3. Salir")
    eleccion_user = int(input())
    print("Opción elegida: ",eleccion_user)
    if(eleccion_user == 1):
        print("¡Comenzamos!")
    if(eleccion_user == 2):
        print("Listado de números: \n1,2,3,4")
    if(eleccion_user == 3):
        print("Hasta la próxima")