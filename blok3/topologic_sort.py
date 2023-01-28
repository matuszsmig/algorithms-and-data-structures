def sort(G, start):
    return DFS(G,start)


def DFS(G,start):
    n = len(G)
    Visited = [False for _ in range(n)]
    Parent = [None for _ in range(n)]
    Distance = [0 for _ in range(n)]
    L = []
    time = 0
    idd = start
    for u in G:
        if Visited[idd] is False:
            DFSVisited(G,idd,Visited,Parent,Distance,time,L)
    L.append(idd)

    i = 0
    while len(L)!=n and i < n:
        if Visited[i] is False:
            DFSVisited(G,i,Visited,Parent,Distance,time,L)
            L.append(i)
        i+=1
    L = L[::-1]
    return L

def DFSVisited(G,u,Visited,Parent,Distance,time,L):
    time+=1
    Visited[u]=True
    Distance[u]=time
    for v in G[u]:
        if Visited[v] is False:
            Parent[v]=u
            DFSVisited(G, v, Visited, Parent, Distance,time,L)
            L.append(v)
    time+=1

G = [[1,2,5],[2,4],[],[],[3,6],[4],[]]
print(sort(G,4))
#a  f ,b ,e ,g, d, c
#[0, 5, 1, 4, 6, 3, 2]