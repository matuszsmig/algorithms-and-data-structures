def countsort(tab, potega):
    tab2 = [0] * 10
    for i in range(len(tab)):
        tab2[tab[i]%(10*potega)//potega] += 1
    for j in range(1, len(tab2)):
        tab2[j] = tab2[j - 1] + tab2[j]
    tab3 = [0] * (len(tab))
    for k in range(len(tab)-1,-1,-1):
        tab3[tab2[tab[k]%(10*potega)//potega]-1] = tab[k]
        tab2[tab[k]%(10*potega)//potega] = tab2[tab[k]%(10*potega)//potega] - 1
    for i in range(len(tab)):
        tab[i]=tab3[i]
    return tab

def radixsort(T):
    maxx=max(T)

    potega = 1

    while maxx/potega > 1:
        countsort(T,potega)
        potega*=10
    return T


tab = [1,5,3,2,43,4,5,222,7]
#tab = [7,2,3,4,2,3,4,1,8,2,3,4,5,7]
print(radixsort(tab))

#print(123%1000//100)