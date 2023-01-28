def countsort(tab,max):
    tab2 = [0]*(max+1)
    for i in range(len(tab)):
        tab2[tab[i]]+=1
    for j in range(1,len(tab2)):
        tab2[j]=tab2[j-1]+tab2[j]
    tab3 = [0]*(len(tab)+1)
    for k in range(len(tab)):
        tab3[tab2[tab[k]]]=tab[k]
        tab2[tab[k]] = tab2[tab[k]]-1
    return tab3


tab = [1,5,2,3,5,6,7,2,2,4,6,7,9,1,2,3,5,6,0,1,2,3,4,6]
print(countsort(tab,max(tab)))