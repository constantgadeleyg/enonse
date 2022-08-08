Non = input("Antre non ou konplè !\nNon : ")

i = 0

while i < len(Non):
    if i == 0 and Non[i].isalpha() == True:
        print(Non[i].upper())
        i += 1
    else :
        if Non[i].isalpha() == True:
            print(Non[i].lower())
            i += 1
        else:
            print(Non[i])
            print(Non[i+1].upper())
            i += 2

        
    