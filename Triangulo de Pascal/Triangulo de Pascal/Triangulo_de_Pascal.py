def TrianguloPascal ():
    lista = []                          #Valores para los elementos de los pisos. "lista" sera la lista que mostrará los numeros de los pisos.
    numero = 0                          #Estos son los numeros de los pisos que se irán sumando para conformar los demas pisos.
    numero2 = 0
    pisos = int(input("¿Cuantos pisos quieres, crack?  "))     #El número de pisos que tendrá el triángulo.


    while numero < pisos:   #Mientras el número sea menor al número de pisos ingresados, el ciclo seguirá.
        numero3 = numero    
        numero2 = 0     

        lista.append(1)         #Se inserta el numero uno, ya que sera el ultimo numero de cada uno de los pisos.
        NuevaLista = lista[:]#Se crea una nueva lista que contendrá los elementos de la primera.
        
        print(lista)

        while numero2 < numero3:  #ciclo que se encarga de hacer la sumatoria de los números de los pisos para conformar los demás.
            lista[numero2 + 1] = NuevaLista[numero2] + NuevaLista[numero2 + 1]

            numero2 = numero2 + 1
                                            #Valores que iran en aumento hasta que superen el numero ingresado, y provocara que se detenga el ciclo.
        numero = numero + 1 

TrianguloPascal()










    

