# Dos elevado a la n

n=int(input("Ingrese el n al cual quiere elevar 2: "))
potencia : int = 1

for i in range(n,n+1):
    potencia *= 2**i

print("Al elevar 2 a la "+str(n)+" nos da como resultado "+str(potencia))