#Ejercicio 5. Imprimir los números de 1 al 100 con while y con for

#While
x = 1

while x <= 100:
    if x == 100:
        print(x)
    else:        
        print(x,end=", ")
    x += 1
    
#For
for i in range(1,101):
    if i == 100:
        print(i)
    else:
        print(i,end=", ")