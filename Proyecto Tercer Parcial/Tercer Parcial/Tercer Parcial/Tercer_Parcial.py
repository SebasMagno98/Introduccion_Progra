import sys
archivo = open("alumnos.txt", "r")
elementos = archivo.readlines()
alumnosLista = list(elementos)
archivo.close()
def main():
    eleccion = str(input("Bienvenido. Escoge la forma en que quieres que se muestren los alumnos.\n Presiona 1 si los quieres ver por orden alfabético.\n presiona 2 si quieres verlos en grupos.\n presiona 3 si quieres verlos ordenados por promedio.\n Presiona 4 si quieres añadir un nuevo alumno. "))
    if eleccion == "1":
        StudentLists()

    elif eleccion == "2":
        OrdenGrupos()

    elif eleccion == "3":
        ordenCali()
   

    else:
        print("Esa no es una opcion valida, prueba con otra.")
        main()
#Funcion de regreso que se manda a llamar al final de cada una de las funciones principales, La cual permite volver al menu o salir del programa.
def VolverMenu():
    opcion = str(input("¿Quieres continuar?\n Presiona 1 si quieres volver al menu.\n Presiona 2 si quires salir."))
    if opcion == "1":
        main()
    elif opcion == "2":
        print("Hasta Luego")
        sys.exit(0)
    else:
        print("Esa no es una opcion posible, por favor escoge 1 o 2")
        VolverMenu()

#Funcion que filtra los alumnos por sus grupos y los mete en un archivo del mismo nombre que el grupo.
def OrdenGrupos(): 
    grupo = str(input("\n¿Que grupo quieres ver?\n 1 = grupo 2016A\n 2 = grupo 2016B\n 3 = grupo 2017A\n 4 = grupo 2017B\n 5 = grupo 2018A\n 6 = grupo 2018B\n"))
    if grupo == "1":
        for item in alumnosLista:
            if "2016A" in item:
                print(item)
                NewFile = open("2016A.txt", "w")
                NewFile.writelines(item)
                NewFile.close()
            VolverMenu()


    elif grupo == "2":
        for item in alumnosLista:
            if "2016B" in item:
                print(item)
                NewFile = open("2016B.txt", "w")
                NewFile.writelines(item)
                NewFile.close()
            VolverMenu()

    elif grupo == "3":
        for item in alumnosLista:
            if "2017A" in item:
                print(item)
                NewFile = open("2017A.txt", "w")
                NewFile.writelines(item)
                NewFile.close()
            VolverMenu()

    elif grupo == "4":
        for item in alumnosLista:
            if "2017B" in item:
                print(item)
                NewFile = open("2017B.txt", "w")
                NewFile.writelines(item)
                NewFile.close()
            VolverMenu()

    elif grupo == "5":
        for item in alumnosLista:
            if "2018A" in item:
                print(item)
                NewFile = open("2018A.txt", "w")
                NewFile.writelines(item)
                NewFile.close()
            VolverMenu()

    elif grupo == "6":
        for item in alumnosLista:
            if "2018B" in item:
                print(item)
                NewFile = open("2018B.txt", "w")
                NewFile.writelines(item)
                NewFile.close()
            VolverMenu()
    else:
        print("Ese número no es válido.")
        OrdenGrupos()



#Clase que almacena a los estudiantes, así como tambien contiene listas con los nombres de los alumnos, y otra lista donde se encuentran sus respectivos promedios.
class Alumno:
    def __init__(self,nombre,promedio,grupo):
        self.nombre = nombre
        self.promedio = promedio
        self.grupo = grupo
        with open("alumnos.txt" , "r") as f:
            listaAlumn = []
            for line in f:
                line = line.rstrip("\\n")
                info = line.split()
                alumno = Alumno(str(info[0]), str(info[1]), str(info[2]))
                alumno.nombre = str(info[0])
                alumno.promedio = str(info[1])
                alumno.grupo = str(info[2])
                listaAlumn.append(alumno)
            for cali in listaAlumn:
                listaCali = []
                calificacion = cali[1]
                listaCali.append(calificacion)

                
#Funcion que organiza a los alumnos por orden alfabético. 
def OrdenAlfa():
    listaNombres = []
    for x in listaAlumn: #Se utilizo el algoritmo de Seleccion, el cual va tomando el valor mínimo de la lista y lo mete en una lista donde estaran el resto de valores una vez se haya organizado.
        listaNombres.append(x) 
        for nombres in range(len(listaNombres)):
            ultInd = nombres
            for j in range(nombres +1, len(listaNombres)):
                if ord(listaNombres[ultInd]) > ord(listaNombres[j]):
                    ultInd = j
        listaNombres[nombres], listaNombres[ultInd] = listaNombres[ultInd], listaNombres[nombres]

    with open("OrdenAlfabético.txt", "w") as Ar:
        Ar.write(listaNombres)
        VolverMenu()

#funcion que organiza los alumnos por promedio. 
def ordenCali():
    for numero in range(1, len(listaCali)): #Se utilizo el algoritmo de Insertion, el cual compara los primeros dos elementos y los organiza a base de comparacion, después pasa al tercer elementos y asi sucesivamente.
        y = numero -1
        sigElem = listaCali[x]

        while (listaCali[y] > sigElem) and (y >= 0):
            listaCali[y+1] = listaCali[y]
            y = y-1
        listaCali[y+1] = sigElem

with open("OrdenPorPromedio.txt" , "w") as Pr:
    Pr.write(listaCali)
    VolverMenu()
    

with open("alumnos.txt" "r") as New:
    line = New.rstrip("\\n")
    estudiantes = line.split()



            

        

            
           
        


if __name__=="__main__":
    main()
