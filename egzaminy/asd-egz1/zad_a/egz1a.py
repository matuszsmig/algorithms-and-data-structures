from egz1atesty import runtests
from queue import PriorityQueue

def snow( S ):
    que = PriorityQueue()
    n = len(S)
    for i in range(n):
        que.put(-S[i])

    suma = 0
    for j in range(n):
        metr = -que.get()
        if metr-j<=0:
            break
        else:
            suma+=metr-j

    return suma

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
#S = [1, 7, 3, 4, 1]
#print(snow(S))
