#3. Sucesión de Fibonacci en Python.
#▻ En matemáticas, la sucesión de Fibonacci es una sucesión
#infinita de números naturales, donde el siguiente numero se
#consigue sumando los dos anteriores.

fibonaci = int(input("Serie de Fibonacci hasta el numero que introduzcas " 
                     "(debe ser de la lista de números de fibonaci) "))
num_total = 0
num1 = 0
num2 = 1

while(num_total < fibonaci):
    num_total = num1 + num2
    num1 = num2
    num2 = num_total
    if(num_total == fibonaci):    
        print(num_total)
    else:
        print(num_total, end=", ")