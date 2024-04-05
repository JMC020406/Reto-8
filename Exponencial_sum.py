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