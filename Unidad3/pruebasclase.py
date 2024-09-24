# def hola(nombre):
#     print("Hola",nombre)

# hola("Pablo")

def sumar(a,b):
    return a + b

resultado = sumar(3,5)
print(sumar(3,5))
print(resultado)

def media_aritmetica(*valores):
    suma = 0
    for num in valores:
        suma += num
    print(f"La media aritmética de los números introducidos es: {suma / len(valores)}")
    
media_aritmetica(2,4,12,42)

def coche(marca,**caracteristicas):
    print(caracteristicas)
    print(f"El coche es de la marca {marca} y tiene las siguientes características: ")
    for valores in caracteristicas.items():
        print(f"{valores[0]}:{valores[1]}")
        
coche("Audi", Modelo = "ACB", Puertas = 5, Color = "Verde")
caracteristicas_coche = dict(Modelo = "ACB", Puertas = 5, Color = "Verde")
# coche("Ford", caracteristicas_coche)