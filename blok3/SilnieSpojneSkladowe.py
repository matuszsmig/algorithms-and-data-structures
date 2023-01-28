def rev(G):
    n = len(G)
    Gprim = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            Gprim[G[i][j]].append(i)
    return Gprim

def DFS(G):
    n = len(G)
    Visited = [False for _ in range(n)]
    L = []
    for i in range(n):
        if Visited[i] is False:
            DFSVisited(G,i,Visited,L)
            L.append(0)
    return L

def DFSVisited(G,u,Visited,L):
    Visited[u]=True
    for v in G[u]:
        if Visited[v] is False:
            DFSVisited(G, v, Visited,L)
            L.append(v)

def DFS2(Gprim,Przet):
    n = len(Gprim)
    Visited = [False for _ in range(n)]
    Odp = [[]]
    for i in range(n):
        if Visited[Przet[i]] is False:
            DFSVisited2(Gprim,Przet[i],Visited,Przet,Odp)
            Odp[len(Odp) - 1].append(Przet[i])
            Odp.append([])
    Odp.remove([])
    return Odp

def DFSVisited2(Gprim,u,Visited,Przet,Odp):
    Visited[u]=True
    for v in Gprim[u]:
        if Visited[v] is False:
            DFSVisited2(Gprim, v, Visited,Przet,Odp)
            Odp[len(Odp)-1].append(v)


G=[[1],[2,4],[0,9],[4,6],[5],[3],[5],[9],[3,7],[10],[5,8]]
Gprim = rev(G)
Przet = DFS(G)[::-1]
#print(Przet)
#[4, 6, 3, 5, 7, 8, 10, 9, 2, 1, 0]
print(DFS2(Gprim,Przet))