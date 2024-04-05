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
