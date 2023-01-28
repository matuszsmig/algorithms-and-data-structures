from testybi import runtests

def rek(S,i,tab):
    if tab[i] != -1:
        return tab[i]
    maxx = 0
    for j in range(i):
        if S[j]=="0":
            maxx = max(maxx,rek(S,j,tab)+1)
        if maxx > 0 and S[j]!="0":
            maxx -=1
    tab[i]=maxx
    return tab[i]


def roznica(S):
    tab = [-1 for _ in range(len(S))]
    flaga = False
    for i in range(len(S)):
        if S[i]=="0":
            flaga=True
            break
    if flaga is False:
        return -1
    maxx = 0
    for i in range(len(S)):
        maxx = max(maxx, rek(S,i,tab))
    return maxx

runtests( roznica )