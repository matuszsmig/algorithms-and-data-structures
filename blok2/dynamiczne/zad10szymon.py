import math

from zad10ktesty import runtests
from math import sqrt

def rek(N,i,Tab,Tab2):
    if N < 0:
        return math.inf
    if N==0:
        return 0
    if N < 3:
        return N
    if Tab[i][N] is not None:
        return Tab[i][N]
    minn = math.inf
    for j in range(i):
        z = rek(N-i*i,j,Tab,Tab2)+1
        if minn > z:
            minn = z
            Tab2[i][N] = (N-i*i,j)
    Tab[i][N]=minn
    return minn

def dywany ( N ):
    minn=999999999999999
    Tab = [[None for _ in range(N+1)] for _ in range(int(sqrt(N))+1)]
    Tab2 = [[None for _ in range(N + 1)] for _ in range(int(sqrt(N)) + 1)]
    for i in range(1,int(sqrt(N))+1):
        z = rek(N,i,Tab,Tab2)
        if z < minn:
            ind = i
            minn = z
    sol = []
    N = N
    Start = (N,ind)
    while Start is not None and Start[0]>=3:
        sol.append(Start[1])
        Start=Tab2[Start[1]][Start[0]]
    N = Start[0]
    while N!=0:
        N-=1
        sol.append(1)
    sol.sort()
    #i = 0
    #N = N
    #sol = []
    #while not (N == 0 or N == 1 or N < 0):
    #    minn = rek(N,i,Tab)+1
    #    war = minn + 2
    #    if i*i <= N:
    #        war = rek(N-i*i,i,Tab)+1
    #    if war < minn:
    #        sol.append(i)
    #        i+=1
    #        N-=i*i
    #    else:
    #        i+=1

    return sol


runtests( dywany )
