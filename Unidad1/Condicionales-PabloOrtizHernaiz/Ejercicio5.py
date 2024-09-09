"""Ejercicio 5: Crear un programa que pida al usuario su DNI sin letra, y la letra.
Calcular si el DNI es correcto. Para calcular la letra del DNI, el número entero del
DNI modulo 23 y el resto es la letra."""

pide_dni = int(input("Introduce tu número de DNI sin letra: "))
pide_letra = input("Introduce la letra de tu DNI en mayúsculas: ")

calculo_letra = pide_dni %23

if(calculo_letra == 0 and pide_letra == "T"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 1 and pide_letra == "R"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 2 and pide_letra == "W"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 3 and pide_letra == "A"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 4 and pide_letra == "G"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 5 and pide_letra == "M"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 6 and pide_letra == "Y"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 7 and pide_letra == "F"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 8 and pide_letra == "P"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 9 and pide_letra == "D"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 10 and pide_letra == "X"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 11 and pide_letra == "B"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 12 and pide_letra == "N"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 13 and pide_letra == "J"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 14 and pide_letra == "Z"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 15 and pide_letra == "S"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 16 and pide_letra == "Q"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 17 and pide_letra == "V"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 18 and pide_letra == "H"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 19 and pide_letra == "L"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 20 and pide_letra == "C"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 21 and pide_letra == "K"):
    print("La letra correspondiente a tu DNI es correcta")
elif(calculo_letra == 22 and pide_letra == "E"):
    print("La letra correspondiente a tu DNI es correcta")
else:
    print("Error")












