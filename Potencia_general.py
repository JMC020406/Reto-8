n=int(input("Ingrese un numero natural (exponente): "))
x=float(input("Ingrese un real (base): "))
potencia:int=1

if n >= 0:
    for n in range (1, n+1):
        potencia = potencia * x

    print(f"La potencia de {x} elevado a la {n} es igual a {potencia}")

else:
    print(f"El valor {n} no es un natural")

