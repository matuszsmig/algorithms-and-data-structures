def DFS(G,start):
    n = len(G)
    Parent = [None for _ in range(n)]
    ToRet = []
    idd = start
    for u in G:
        DFSVisited(G,idd,Parent,ToRet)
    ToRet.append(idd)
    return ToRet

def DFSVisited(G,u,Parent,ToRet):
    for v in G[u]:
        Parent[v]=u
        G[v].remove(u)
        G[u].remove(v)
        DFSVisited(G, v, Parent,ToRet)
        ToRet.append(v)

G = [[1,2],[0,2,3,5],[0,1,3,5],[1,2,4,5],[3,5],[1,2,3,4]]
#G[1].remove(2)
#print(G)
print(DFS(G,5))