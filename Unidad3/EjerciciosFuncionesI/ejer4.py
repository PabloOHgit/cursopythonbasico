# 4. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje
# indicando si la dirección es válida o no, valiéndose de una función para
# decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

def comprobar_email(email):
    if "@" in email:
        respuesta = "Tu email es correcto, contiene arroba"
    else:
        respuesta = "Tu email no es correcto, no contiene arroba"
    print(respuesta)
    
email = input("Escribe tu email para comprobar si es correcto: ")
comprobar_email(email)