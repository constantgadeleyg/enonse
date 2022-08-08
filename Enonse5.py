import operator


Chenn = input("Mete yon chenn ki gen nonb selman\nChenn : ")

Tot_2_Car = 0
ChennDiv = Chenn.split()

LisPouMiltip = []

for i in range(len(ChennDiv)):
    if len(ChennDiv[i]) <  2 :
        LisPouMiltip.append(int(ChennDiv[i]))
    else:
        for a in ChennDiv[i]:
            Tot_2_Car += int(a)
        LisPouMiltip.append(Tot_2_Car)
        Tot_2_Car = 0

Total = 1

for x in LisPouMiltip :
    Total = Total * x


    
print(LisPouMiltip)
print(Total)