def fibonacci():

	print("Secuencia Fibonacci")
	Num=0
	Num1=0
	Num2=1
	print(Num)
	print(Num2)
	for NumerosLocos in range (0 , 8):
		Num=Num1
		Num1=Num2
		Num2=Num + Num1
		print(Num2)

fibonacci()		