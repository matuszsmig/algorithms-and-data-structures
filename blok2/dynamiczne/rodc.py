def rek(T, i, tab):
    if i == 0:
        tab[i]=0
        return 0
    if i == 1:
        tab[i] = T[0]
        return T[0]
    maxx = 0
    for j in range(1,i+1):
        maxx = max(maxx, T[j-1]+rek(T,i-j,tab))
    tab[i] = maxx
    return tab[i]

def zad(T,n):
    tab = [0 for _ in range(n+1)]
    maxx = 0
    for i in range(n+1):
        maxx = max(maxx,rek(T,i,tab))
    return maxx

N = 8
P = [1,5,8,9,10,17,17,20]
print(zad(P,N))