#3. Crea un programa que pida al usuario una frase y luego:
# ▻ Convierta toda la frase a minúsculas.
# ▻ Cuente cuántas veces aparece la letra "a" en la frase.
# ▻ Imprima la frase sin las vocales.

frase = input("Introduce un texto: ")

print(frase.lower())

print(frase.count("a"))

for letra in frase:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        continue
    print(letra,end="")
    
for letra in frase:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        frase.replace("a"," ")
    print(letra,end="")

