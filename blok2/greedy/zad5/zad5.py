from zad5testy import runtests
from queue import PriorityQueue


def plan(T):
    n = len(T)
    Odp = [0]
    energia = PriorityQueue()
    E = T[0]
    i = 1
    while True:
        if i > n-1:
            break
        if i > E:
            toE, toAns = energia.get()
            Odp.append(-toAns)
            E+=(-toE)
        if T[i]>0:
            energia.put((-T[i],-i))
        i+=1
    Odp.sort()
    return Odp


T = [3,0,2,1,0,2,5,0]
print(plan(T))
runtests( plan, all_tests = True )