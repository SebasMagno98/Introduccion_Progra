def multiplicacion(numero, numveces, n):
    if numero != n * numveces:
        numero+=n
        multiplicacion(numero, numveces, n)
    elif numero == n * numveces:
        print(numero)
numero = int(input("numero a multiplicar: \n"))
numveces = int(input("Numero por el cual quieres multiplicar: \n"))
n=numero
multiplicacion(numero, numveces, n)