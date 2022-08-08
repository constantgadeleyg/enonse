def Asterisk(Chenn, ChennAste="", Voy = "aeiouyAEIOUY"):
	for i in Chenn:
		if i in Voy:
			ChennAste += i
		else:
			ChennAste += "*"
			
	return ChennAste
	

print(Asterisk("Koman ou ye"))