import random 
archivo = open("palabras.txt", "r")
aleatoria = archivo.readlines()
palabra= str(random.choice(aleatoria))
archivo.close()
numLetras = len(palabra) - 1
abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
adivinanza = []
letrasUsadas =[]



print(palabra)

for letra in palabra:
    adivinanza.append("-")
print("Preparate campeon, que esta palabra tiene",numLetras, "letras")  

print(adivinanza)



def ahorcado():
    intentos=5


    while (intentos > 0):

        adivinarLetras = input("Ingresa una letra, crack \n").lower()
        if  adivinarLetras not in abecedario:
            print("Solo letras, rufian, nada de numeros, y tampoco mas de una letra, plox.")
        elif adivinarLetras in letrasUsadas:
            print("Ya usaste esa letra, campeon")
        else:

            letrasUsadas.append(adivinarLetras)

            if adivinarLetras in palabra:
                print("Muy bien, crack. Acertaste, sigue asi.")
                for elemento in range(0, numLetras):
                    if palabra[elemento] == adivinarLetras:
                        adivinanza[elemento] = adivinarLetras
                        print(adivinanza)

                if not "-"  in adivinanza:
                    print("Excelente, acertaste todas crack, bien hecho.")
                    break
            else:
                print("Fallaste, cuidado crack. Te quedan,", intentos, "intentos.")
                intentos = intentos - 1 
                if intentos == 0:
                    print("Perdiste, ya no te quedan mas turnos, la palabra secreta era:", palabra)

            

ahorcado()
print("Acabo el juego")
