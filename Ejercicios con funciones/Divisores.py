def divisores (numerador):
	divisor = 1

	while divisor <= (numerador):
		if numerador == divisor:
			break

		
		if numerador % divisor == 0:
			print(divisor)
			divisor += 1


		else:
			divisor += 1 

divisores(int(input(" ingresa un numero crack:  ")))	

