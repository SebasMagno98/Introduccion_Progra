import random 
archivo = open("palabras.txt", "r")
aleatoria = archivo.readlines()
palabra = str(random.choice(aleatoria))
archivo.close()
numLetras = len(palabra) - 1
abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ"
adivinanza = []
letrasUsadas = []

print(palabra)

for letra in palabra: 
    if letra != '\n':
        adivinanza.append(letra)
        


for letra in palabra:
    adivinanza.append("-")
print("Prepárate campeón, que esta palabra tiene",numLetras, "letras")    

print(adivinanza)

def juego():
    intentos = 5

    while intentos > 0:

        adivinarLetras = input("Ingresa una letra, crack \n").lower()
        if adivinarLetras not in abecedario:
            print("Solo letras, rufián, nada de numeros plox.")
        elif adivinarLetras in letrasUsadas:
            ("Ya usaste esa letra, campeón, intenta con otra.")
        else:

            letrasUsadas.append(adivinarLetras)

            if adivinarLetras in palabra:
                print("muy bien, crack. Acertaste, sigue asi.")
                for elemento in range (0,numLetras ):
                    if palabra[elemento] == adivinarLetras:
                        adivinanza[elemento] = adivinarLetras
                        print(adivinanza)                        

                if not "-" in adivinanza:
                    print("Has ganado, eres toda una máquina en esto.")
                    break
            else:
                print("Fallaste, cuidado crack. Te quedan", intentos, "intentos")
                intentos = intentos - 1
                if intentos == 0:
                    print("Perdiste, ya no te quedan mas turnos, la palabra secreta era", palabra)


juego()

