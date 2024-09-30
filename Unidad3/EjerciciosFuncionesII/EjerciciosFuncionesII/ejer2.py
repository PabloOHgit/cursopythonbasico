# 2. Crea un programa de cifrado y descifrado, utilizando el Método Cesar. Que consiste en
# desplazar la letra original x puestos hacia la derecha.

# a. Por ejemplo, utilizando la frase: El perro y haciendo 2 desplazamientos a la
# derecha quedaría Gn rgttq.
# b. Recordar que Python es Case Sensitive (distingue entre mayúsculas y
# minúsculas)
# c. Se puede elegir el desplazamiento que se quiera

#CIFRADO CESAR

def cifrado_cesar(mensaje,desplazamiento):
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mensaje_cifrado = ""
    
    for letra in mensaje.upper():
        if letra in alfabeto:
            indice = (alfabeto.index(letra)+desplazamiento) %26
            mensaje_cifrado += alfabeto[indice]
        else:
            mensaje_cifrado += letra
        
    return mensaje_cifrado

def descifrar_cesar(mensaje,desplazamiento):
    return cifrado_cesar(mensaje,-desplazamiento)
    
mensaje = input("Introduce mensaje: ")
desplazamiento = int(input("Introduce desplazamiento: "))

print(cifrado_cesar(mensaje,desplazamiento))
mensaje_descifrar = cifrado_cesar(mensaje,desplazamiento)
print(descifrar_cesar(mensaje_descifrar,desplazamiento))