Sekans = [0,1,2,3,4]

L = len(Sekans)
TB = 0
i = 0
TA = 0


while i < L:
    if i == 0 :
        Sekans = Sekans[L+TA+TA:TB-L-1 + TA:-1]
        print(Sekans)
        TB += 1
        TA -= 1
        i += 1
    if i == 1 :
        Sekans = Sekans[L+TA+TA:TB-L-1 + TA:-1] + Sekans[L-i:]
        print(Sekans)
        TB += 1
        TA -= 1
        i += 1
    if i == 2 :
        Sekans = Sekans[L+TA+TA+1:TB-L-1 + TA:-1] + Sekans[L-i:]
        print(Sekans)
        TB += 1
        TA -= 1
        i += 1
    if i == 3 :
        Sekans = Sekans[L+TA+TA+2:TB-L-1 + TA:-1] + Sekans[L-i:]
        print(Sekans)
        TB += 1
        TA -= 1
        i += 1
    if i == 4 :
        Sekans = Sekans[L+TA+TA+3:TB-L-1 + TA:-1] + Sekans[L-i:]
        print(Sekans)
        TB += 1
        TA -= 1
        i += 1
        

print("\n",Sekans.index(3))
    
    
    
    
    