# Ejercicio 1. Hemos comenzado a trabajar en una empresa del sector farmacéutico
# llamada BioNTech. Nos vamos a ocupar de ciertos análisis bioinformáticos. La primera
# ocupación que tenemos a nuestra llegada es trabajar sobre la siguiente cadena de ARN:
# “AOUCUGGUGGGGAUCUATTAGGUCGGUGGATTGCUGAUTTUGGUCGOGGAGCOTUAUG
# GUCCUGGATGATCUGGUCCAGGTOGGUCGUGGUGGAGGTOACCGTAOGGUGGUCUUGG
# UCAUGGUACCUGGUGTTAOCCUCCUGGUGGUTAOGGCCUGGOTGCAGGAGGUGGUCCUG
# GTOAUGGOTGACUGG”
# Cada carácter de la cadena representa un nucleótido que forma parte del ARN. Sabemos
# que ARN esta formado por 4 nucleótidos: Adenina(A), Guanina(G), Citosina(C) y Uracilo
# (U).
# La empresa está interesada en saber cuántas tripletas de nucleótidos presentes en la
# cadena van a codificar en aminoácido triptófano (UGG). Aparte de eso ha habido ciertos
# errores en la secuencia y han aparecido signos extraños (T y O) que no pertenecen al
# ARN.
# Escribe un programa que primero limpie la cadena de caracteres extraños y a
# continuación cuente el numero de tripletas UGG presentes.

cadena_arn = "AOUCUGGUGGGGAUCUATTAGGUCGGUGGATTGCUGAUTTUGGUCGOGGAGCOTUAUGGUCCUGGATGATCUGGUCCAGGTOGGUCGUGGUGGAGGTOACCGTAOGGUGGUCUUGGUCAUGGUACCUGGUGTTAOCCUCCUGGUGGUTAOGGCCUGGOTGCAGGAGGUGGUCCUGGTOAUGGOTGACUGG"
cadena_reparada = cadena_arn.replace("T" and "O","")
# cadena_reparada = cadena_reparada.replace("O","")
tripletas = cadena_reparada.count("UGG")
print(tripletas)