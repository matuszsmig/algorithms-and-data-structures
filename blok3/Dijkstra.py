from queue import PriorityQueue
from math import inf

def RedańskiSzpieg(G,s):
    que = PriorityQueue()
    maxx=0
    for i in range(len(G)):
        if G[i][1] > maxx:
            maxx = G[i][1]
    Distance = [inf for _ in range(maxx+1)]
    Prepered = [False for _ in range(maxx+1)]
    Parent = [None for _ in range(maxx+1)]
    Distance[s] = 0

    que.put((0,s))

    while not que.empty():
        w, u = que.get()
        i = 0
        while i != len(G) and G[i][0]!=u:
            i += 1
        while i != len(G) and G[i][0]==u:
            v = G[i][1]
            w = G[i][2]
            if Prepered[v]==False:
                if Distance[v] > Distance[u] + w:
                    Distance[v] = Distance[u] + w
                    Parent[v] = u
                que.put((Distance[v],v))
            i += 1
        Prepered[u]=True

    return Distance


G = [[0,1,1],[0,7,2],[1,0,1],[1,2,2],[1,4,3],[2,1,2],[2,3,5],[3,2,5],[3,6,1],[4,1,3],[4,7,1],[4,5,3],[5,4,3],[5,6,8],[5,8,1],[6,5,8],[6,3,1],[6,8,4],[7,0,2],[7,4,1],[7,8,7],[8,7,7],[8,6,4],[8,5,1]]
print(RedańskiSzpieg(G,0))

#if Distance[v] > Distance[u] + w:
#    Distance[v] = Distance[u] + w
#    Parent[v] = u