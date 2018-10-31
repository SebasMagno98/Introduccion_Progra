def Listas ():
	ListaA = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	ListaB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	ListaTres = []
	for ListaC in ListaA and ListaB: 
		if ListaC in ListaA and ListaB:
			ListaTres.append(ListaC)

	print(ListaTres)
	
Listas()			