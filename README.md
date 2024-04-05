# Reto-8
## Bucles 2
Bucles 2, que más se puede decir.

### Punto 1 / Listado del 1 al 100 con sus respectivos cuadrados.
```py
def cuadradonumero (i=int)->int:
    return (i**2)

#numero del 1 al 100 y sus cuadrados

if __name__ == "__main__":

    i:int=1

print("Lista de numeros del 1 al 100 y sus cuadrados:")
print("INICIO")

while i<=100:
    cuadrado=cuadradonumero(i)
    print(str(i)+" , "+str(cuadrado))
    i+=1

print ("FIN")
```

### Punto 2 / Listado de numeros pares e impares del 1 hasta el 1000.
```py
#listado de numeros impares y pares

i:int=1

print("Listado de numeros impares del 1 hasta el 999:")
print("INICIO")

while i<1000:
    if i % 2 != 0:
        print(str(i))
    i += 1

print("FIN")

i -= 998

print("Listado de numeros pares del 2 hasta el 1000:")
print("INICIO")

while i<=1000:
    if i % 2 == 0:
        print(str(i))
    i += 1

print("FIN")
```

### Punto 3 / Listado descendente de pares de un *n* hasta 2.
```py
#listado descendente de numero pares desde un n hasta el 2

n=int(input("Ingrese un numero natural: "))

print("Listado de numeros pares descendentemente desde "+str(n)+" hasta 2:")
print("INICIO")

while n>=2:
    if n % 2 == 0:
        print(n)
    n -= 1

print("FIN")
```

### Punto 4 / Numeros del 1 a *n* cada uno con su factorial.
```py
# Listado del 1 hasta un n factorial

num=int(input("Ingrese el numero natural del cual quiere saber su factorial: "))
i:int=1
factorial:int=1

print("Lista de factoriales de 1 hasta "+str(num)+":")
print("INICIO")
while i <= num:
    factorial *= i
    print (str(i)+"! = "+str(factorial))
    i += 1

print("FIN")
```

### Punto 5 / 2 elevado a la *n* con ciclos for.
```py
# Dos elevado a la n

n=int(input("Ingrese el n al cual quiere elevar 2: "))
potencia : int = 1

for i in range(n,n+1):
    potencia *= 2**i

print("Al elevar 2 a la "+str(n)+" nos da como resultado "+str(potencia))
```

### Punto 6 / Potencia de *x* a la *n* usando ciclos for y evitando el uso de la potencia.
```py
n=int(input("Ingrese un numero natural (exponente): "))
x=float(input("Ingrese un real (base): "))
potencia:int=1

if n >= 0:
    for n in range (1, n+1):
        potencia = potencia * x

    print(f"La potencia de {x} elevado a la {n} es igual a {potencia}")

else:
    print(f"El valor {n} no es un natural")
```

### Punto 7 / Tablas de multiplicar del 1 al 9.
```py
print("Tablas de multiplicar del 1 al 9: ")
for i in range (1, 10):
    print()
    print(f"Tabla del {i}")
    for j in range (1, 10):
        multiplicacion = i * j
        print (f"{i} x {j} = {multiplicacion}")
```

### Punto 8 / Sumatoria aproximada a la funcion *exponencial*.
```py
import math

# Para que la aroximación tenga una desviación menor del 0.1% debe ser:
# El x >= 5 y el n >= 12

x=float(input("Ingrese el exponente: "))
n=int(input("Numero de terminos (máximo 170): "))
factorial:int=1
termino:float=0
sumatoria:float=0

print(f"Valor real = {math.e**x}")

for i in range (1, n+1):
    factorial *= i
    termino = (x**i)/factorial
    sumatoria += termino

print (f"Valor aproximado = {sumatoria}")

diferencia = (sumatoria/(math.e**x))*100

print (f"Diferencia porcentual = {diferencia}")
```

### Puntos 9 y 10 / Sumatorias aproximadas de funcion *Seno* y funcion *ArcTan*.
Sencillamente no se lograron hacer.
