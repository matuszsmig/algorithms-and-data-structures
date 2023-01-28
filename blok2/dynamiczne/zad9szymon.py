from zad9ktesty import runtests
from math import inf

def rek(T, g, d, i,Tabg1,Tabd1):
    if Tabg1[g][i] is not None:
        return Tabg1[g][i]
    if Tabd1[d][i] is not None:
        return Tabd1[d][i]
    if i == len(T):
        return 0
    if T[i] > g and T[i] > d:
        return 0
    if T[i] > g:
        maxx = rek(T, g, d-T[i], i+1,Tabg1,Tabd1)+1
        Tabg1[g][i] = maxx
        return maxx
    if T[i] > d:
        maxx = rek(T, g-T[i], d, i+1,Tabg1,Tabd1)+1
        Tabd1[d][i] = maxx
        return maxx
    p1 = rek(T, g - T[i], d, i + 1,Tabg1,Tabd1) + 1
    p2 = rek(T, g, d - T[i], i + 1,Tabg1,Tabd1) + 1
    if p1>p2:
        maxx = p1
        Tabg1[g][i]=maxx
    else:
        maxx=p2
        Tabd1[d][i] = maxx
    return maxx


def prom(P, g, d):
    n = len(P)
    Tabg1 = [[None for _ in range(n)]for _ in range(g+1)]
    Tabd1 = [[None for _ in range(n)] for _ in range(d + 1)]
    maxx = rek(P,g, d, 0,Tabg1,Tabd1)
    i = 0
    odp = []
    odp2 = []
    while i < len(P) and (g >=P[i] or d >= P[i]):
        if P[i]>g:
            w1 = 0
            w2 = 1
        elif P[i]>d:
            w1 = 1
            w2 = 0
        else:
            w1 = rek(P,g-P[i],d,i+1, Tabg1,Tabd1)
            w2 = rek(P,g,d-P[i],i+1, Tabg1,Tabd1)

        if w1 > w2:
            odp.append(i)
            g -= P[i]
        else:
            odp2.append(i)
            d -= P[i]
        i+=1
    if maxx - 1 in odp:
        return odp
    else:
        return odp2

runtests ( prom )