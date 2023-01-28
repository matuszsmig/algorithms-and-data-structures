from collections import deque
def BFS(G, p):
    Visited = [False for _ in range(len(G))]
    Distance = [0 for _ in range(len(G))]
    Parents = [None for _ in range(len(G))]
    Que = deque()
    Que.append(p)
    Visited[p] = True
    while Que:
        u = Que.popleft()
        for v in G[u]:
            if Visited[v] is False:
                Visited[v] = True
                Distance[v]=Distance[u]+1
                Parents[v] = u
                Que.append(v)
    return Parents


#[0, 1, 2, 3, 5, 4][None, 0, 1, 2, 0, 4]
T = [[1, 4], [0, 2], [1, 3], [2, 5], [0, 5], [4, 3]]
print(BFS(T,0))
print(BFS(T,2))