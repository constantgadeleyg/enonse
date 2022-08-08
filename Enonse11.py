def MaxTab(Tablo):
    Max = Tablo[0]
    for i in Tablo:
        if i > Max :
            Max = i
    return Max
        
        
        
def MinTab(Tablo):
    Min = Tablo[0]
    for i in Tablo:
        if i < Min :
            Min = i
            
    return Min    

print("Max Tablo =",MaxTab([1,2,3,4]),"\nMin Tablo =",MinTab([1,2,3,4]))