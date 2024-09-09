#Ejercicio 3: Pedir al usuario 5 números y decir si son par o impar.

print("\nVamos a realizar un ejercicio en el que vas a "
      "introducir 5 números y diremos si es par o impar")
contador = 0
while(contador < 5):
    numero = int(input("\nIntroduce el número "))
    if(numero %2 == 0):
        print("El número es par")
    else:
        print("El número es impar")
    contador += 1
else:
    print("\nYa has introducido 5 números, hemos acabado el ejercicio")