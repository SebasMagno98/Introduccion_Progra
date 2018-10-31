import random
def listaAleatorios(x):
      lista = [0]  * x
      for y in range(x):
          lista[y] = random.randint(1,100)
      return lista
 
print listaAleatorios(13)


import random
def listaAleatorios2(n):
      lista2 = [0]  * n
      for i in range(n):
          lista2[i] = random.randint(1,100)
      return lista2
 
print listaAleatorios2(13)



h=listaAleatorios(13)	
k=listaAleatorios2(13)
def nuevaLista():
	ListaA = h
	ListaB = k
	ListaC = [h + k]
	
	print(ListaC)
nuevaLista()			

