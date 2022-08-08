LisMiltip_aNon_b = []
LisMiltip_bNon_a = []
LisMiltip_aAk_b = []
LisNonMiltip_aAk_b = []


def NonbYo(a,b,x,y):
    for i in range(x,y+1):
        if i%a == 0 and i%b != 0:
            LisMiltip_aNon_b.append(i)
        elif i%b == 0 and i%a != 0:
            LisMiltip_bNon_a.append(i)
        elif i%a == 0 and i%b == 0:
            LisMiltip_aAk_b.append(i)
        else :
            LisNonMiltip_aAk_b.append(i)
            
            
NonbYo(2,3,1,20)
            
print(LisMiltip_aNon_b,"-> Total nonb :", len(LisMiltip_aNon_b))
print(LisMiltip_bNon_a,"-> Total nonb :", len(LisMiltip_bNon_a))
print(LisMiltip_aAk_b,"-> Total nonb :", len(LisMiltip_aAk_b))
print(LisNonMiltip_aAk_b,"-> Total nonb :", len(LisNonMiltip_aAk_b))