import string

def Dekripte(Chenn):
	
	Alpha = string.ascii_uppercase
	Idx = 0
	Output = ""
	
	for i in range(len(Chenn.split())):
		if Chenn.split()[i][0] == ">":
			Idx = Alpha.index(Chenn.split()[i][-1]) + int(Chenn.split()[i][1:-1])
			Output += Alpha[Idx]
			Idx = 0
		elif Chenn.split()[i][0] == "<":
			Idx = Alpha.index(Chenn.split()[i][-1]) - int(Chenn.split()[i][1:-1])
			Output += Alpha[Idx]
			Idx = 0
				
	print(Output)
		
		
Dekripte("<1T >7H >3C <5Y >13J <2C <5W >4A")