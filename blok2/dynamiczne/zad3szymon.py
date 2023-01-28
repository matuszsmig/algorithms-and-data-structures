from zad3ktesty import runtests
from math import inf

def rek(T,k,i,Tab):
    if i >= len(T):
        return 0
    minn = inf
    for j in range(k+i,i,-1):
        minn = min(minn,rek(T,k,j,Tab)+T[j-k])
    return minn


def ksuma(T, k):
    Tab = [[None for _ in range(len(T))]for _ in range(k+1)]
    n = len(T)
    minn = inf
    for i in range(k-1,-1,-1):
        minn = min(minn,rek(T,k,i,Tab))
    return minn


runtests(ksuma)