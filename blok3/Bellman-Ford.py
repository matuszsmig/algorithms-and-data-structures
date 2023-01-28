from math import inf

def BellmanFord(G,s):
    maxx = 0
    for i in range(len(G)):
        if G[i][1] > maxx:
            maxx = G[i][1]
    Distance = [inf for _ in range(maxx+1)]
    Parent = [None for _ in range(maxx + 1)]
    Distance[s]=0
    for _ in range(maxx):
        for i in range(len(G)):
            if Distance[G[i][0]] != inf and Distance[G[i][1]] > Distance[G[i][0]] + G[i][2]:
                Distance[G[i][1]] = Distance[G[i][0]] + G[i][2]
        for i in range(len(G)):
            if Distance[G[i][0]] != inf and Distance[G[i][1]] > Distance[G[i][0]] + G[i][2]:
                return False
    return Distance





G = [[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]
print(BellmanFord(G,0))