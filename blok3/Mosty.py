def DFS(G):
    n = len(G)
    Visited = [False for _ in range(n)]
    Parent = [None for _ in range(n)]
    Low = [None for _ in range(n)]
    D = []
    Bridges = []
    for i in range(n):
        if Visited[i] is False:
            DFSVisited(G,i,Visited,Parent,D,Low)
    for i in range(n):
        if D[i]==Low[i] and Parent[i]!=None:
            Bridges.append((i,Parent[i]))
    return Bridges

def DFSVisited(G,u,Visited,Parent,D,Low):
    Visited[u]=True
    D.append(u+1)
    Low[u]=u+1
    for v in G[u]:
        if Visited[v] is False:
            Parent[v]=u
            DFSVisited(G, v, Visited, Parent,D,Low)
            Low[v] = D[v]
        else:
            Low[v]=min(D[v],Low[u])
            while v!=0:
                Low[Parent[v]]= min(Low[v],Low[Parent[v]])
                v = Parent[v]



G = [[1,2],[0,3],[0,3,4],[1,2,5],[2],[3,6,7],[5,7],[5,6]]
print(DFS(G))