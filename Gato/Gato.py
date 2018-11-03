espacio = ["", " ", " ", " ", " ", " ", " " , " ", " ", " "]
espacios = [1,2,3,4,5,6,7,8,9]



def main():
    eleccion = int(input("Elige 1 para un PVP loco o Elige 2 para 1v1 con la PC"))
    if eleccion == 1:
        gatoPVP()
    if eleccion == 2:
        PC1v1()    
    
    


def gato():
    print("   "+espacio[1], "|" +espacio[2],  "|"      +espacio[3],  "")
    print('   -----------')
    print("   "+espacio[4], "|" +espacio[5],  "|"      +espacio[6],  "")
    print('   -----------')
    print("   "+espacio[7], "|" +espacio[8],  "|"      +espacio[9],  "")


def gatoPVP(): 
    TicTacToe = True
    while TicTacToe == True:
        
        gato()
#Turno de Jugador 1 que será "X"
        jugada = int(input("Ingresa un numero del 1 al 9, jugador 1: \n"))

        if espacio[jugada] == " ":
            espacio[jugada] = "X"
        else:
            ("Espacio ocupado, pillo. Intenta de nuevo plox")
        
        
#Condiciones de Victoria para "X"
        if (espacio[1] == "X" and espacio[2] == "X" and espacio[3] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[4] == "X" and espacio[5] == "X" and espacio[6] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[7] == "X" and espacio[8] == "X" and espacio[9] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[1] == "X" and espacio[5] == "X" and espacio[9] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[3] == "X" and espacio[5] == "X" and espacio[7] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[1] == "X" and espacio[4] == "X" and espacio[7] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[3] == "X" and espacio[6] == "X" and espacio[9] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[2] == "X" and espacio[5] == "X" and espacio[8] == "X"):
        
            print("Feliciades, X ganó")
            break
        gato()



      

#Turno de jugador 2 que será "O"
        jugada = int(input("Ingresa un numero del 1 al 9, jugador 2:  "))
        if espacio[jugada] == " ":
            espacio[jugada] = "O"
        else:
            ("Espacio ocupado, pillo. Intenta de nuevo plox")


#Condiciones de Victoria de "O"
        if (espacio[1] == "O" and espacio[2] == "O" and espacio[3] == "O"):
            gato()
            print("Feliciades, O ganó")
            break
        if (espacio[4] == "O" and espacio[5] == "O" and espacio[6] == "O"):
            gato()
            print("Feliciades, O ganó")
            break
        if (espacio[7] == "O" and espacio[8] == "O" and espacio[9] == "O"):
            gato()
            print("Feliciades, O ganó")
            break
        if (espacio[1] == "O" and espacio[5] == "O" and espacio[9] == "O"):
            gato()
            print("Feliciades, O ganó")
            break
        if (espacio[3] == "O" and espacio[5] == "O" and espacio[7] == "O"):
            gato()
            print("Feliciades, O ganó")
            break
        if (espacio[1] == "O" and espacio[4] == "O" and espacio[7] == "O"):
            gato()
            print("Feliciades, O ganó")
            break
        if (espacio[3] == "O" and espacio[6] == "O" and espacio[9] == "O"):
            gato()
            print("Feliciades, O ganó")
            break
        if (espacio[2] == "O" and espacio[5] == "O" and espacio[8] == "O"):
            gato()
            print("Feliciades, O ganó")
            break    

        

def PC1v1():
    import random

    TicTacToe = True
    while TicTacToe == True:
        gato()
        
#Turno de Jugador  que será "X"
        jugada = int(input("Ingresa un numero del 1 al 9, jugador 1: \n"))

        if espacio[jugada] == " ":
            espacio[jugada] = "X"
        else:
            ("Espacio ocupado, pillo. Intenta de nuevo plox")
        
        
#Condiciones de Victoria para "X"
        if (espacio[1] == "X" and espacio[2] == "X" and espacio[3] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[4] == "X" and espacio[5] == "X" and espacio[6] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[7] == "X" and espacio[8] == "X" and espacio[9] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[1] == "X" and espacio[5] == "X" and espacio[9] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[3] == "X" and espacio[5] == "X" and espacio[7] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[1] == "X" and espacio[4] == "X" and espacio[7] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[3] == "X" and espacio[6] == "X" and espacio[9] == "X"):
        
            print("Feliciades, X ganó")
            break
        if (espacio[2] == "X" and espacio[5] == "X" and espacio[8] == "X"):
        
            print("Feliciades, X ganó")
            break
    
    
  

#Turno de la PC que será "O"
        jugador = "O"
        jugada = random.randint(1,9)
        if espacio[jugada] == " ":
            espacio[jugada] = "O"
        else:
            print("intenta de nuevo.")
        

#Condiciones de Victoria de "O"
        if (espacio[1] == "O" and espacio[2] == "O" and espacio[3] == "O"):
            
            print("Feliciades, O ganó")
            break
        if (espacio[4] == "O" and espacio[5] == "O" and espacio[6] == "O"):
            
            print("Feliciades, O ganó")
            break
        if (espacio[7] == "O" and espacio[8] == "O" and espacio[9] == "O"):
            
            print("Feliciades, O ganó")
            break
        if (espacio[1] == "O" and espacio[5] == "O" and espacio[9] == "O"):
            
            print("Feliciades, O ganó")
            break
        if (espacio[3] == "O" and espacio[5] == "O" and espacio[7] == "O"):
            
            print("Feliciades, O ganó")
            break
        if (espacio[1] == "O" and espacio[4] == "O" and espacio[7] == "O"):
            
            print("Feliciades, O ganó")
            break
        if (espacio[3] == "O" and espacio[6] == "O" and espacio[9] == "O"):
            
            print("Feliciades, O ganó")
            break
        if (espacio[2] == "O" and espacio[5] == "O" and espacio[8] == "O"):
            
            print("Feliciades, O ganó")
            break
        
        

main()          