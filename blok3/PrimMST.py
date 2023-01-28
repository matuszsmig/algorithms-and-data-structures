from math import inf

def Prim(G,s):
    N = len(G)
    G.sort()
    maxx = max(max(G))
    n = maxx +1
    W = [inf for _ in range(n)]
    Parent = [None for _ in range(n)]
    Przetworzone = [False for _ in range(n)]
    W[s]=0
    Przetworzone[s] = True

    for i in range(len(Przetworzone)):
        for v in range(N):
            if G[v][0] == s:
                break
        cp = v
        while v < N and G[v][0] == s:
            w = v
            while w < N and G[w][0]==s:
                if Przetworzone[G[w][1]] == False and W[G[w][1]] > G[w][2]:
                    W[G[w][1]]=G[w][2]
                w+=1
            v+=1
        minn = inf
        while cp < N and G[cp][0] == s:
            if Przetworzone[G[cp][1]] == False and W[G[cp][1]]<minn:
                minn=W[G[cp][1]]
                tmp = G[cp][1]
            cp+=1
        s=tmp
        Przetworzone[s]=True
    sum = 0
    for i in range(len(W)):
        sum+=W[i]
    return sum

def Prim2(G,start):
    N = len(G)
    maxx = max(max(G))
    n = maxx + 1
    W = [inf for _ in range(n)]
    Przetworzone = [False for _ in range(n)]
    Parent = [None for _ in range(n)]
    W[start] = 0
    Przetworzone[start] = True
    for i in range(n):
        minn = inf
        for u in range(N):
            if Przetworzone[G[u][0]] == True and Przetworzone[G[u][1]] == False and G[u][2] < minn:
                minn = G[u][2]
                minn_ind = u
        u = minn_ind
        Przetworzone[G[u][1]]=True
        W[G[u][1]]=G[u][2]
        Parent[G[u][1]]=G[u][0]

    return Parent



G = [[0,1,1], [0,2,3],[1,0,1],[1,3,2],[1,4,4],[2,0,3],[2,3,1],[2,4,2],[3,1,2],[3,2,1],[3,5,1],[4,1,4],[4,2,2],[4,5,3],[5,4,3],[5,3,1]]
print(Prim2(G,0))