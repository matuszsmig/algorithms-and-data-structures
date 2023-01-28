def DFS(G):
    n = len(G)
    Visited = [False for _ in range(n)]
    Parent = [None for _ in range(n)]
    Distance = [0 for _ in range(n)]
    time = 0
    for i in range(n):
        if Visited[i] is False:
            DFSVisited(G,i,Visited,Parent,Distance,time)
    return Distance

def DFSVisited(G,u,Visited,Parent,Distance,time):
    time+=1
    Visited[u]=True
    Distance[u]=time
    for v in G[u]:
        if Visited[v] is False:
            Parent[v]=u
            DFSVisited(G, v, Visited, Parent, Distance,time)
    time+=1



T = [[1, 4], [0, 2], [1, 3], [2, 5],[0, 5],[4, 3]]
print(DFS(T))