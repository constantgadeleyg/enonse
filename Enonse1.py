# Verifye pot ki louvri a

AdresIP = input("Antre adrès IP ou a !\nAdrès IP : ")
PotOuve = 0
LisKonpozanIP = AdresIP.replace(".","")


for i in LisKonpozanIP:
    PotOuve += int(i) * int(LisKonpozanIP[0])


print("Pòt ki ouvè a se : ",PotOuve)