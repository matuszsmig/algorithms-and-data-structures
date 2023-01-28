from math import inf

def FloydWarshall(G):
    n = len(G)
    odp = G
    for k in range(n):
        for u in range(n):
            for v in range(n):
                odp[u][v] = min(odp[u][v], odp[k][v] + odp[u][k])
    return odp



graph = [[0, 5, inf, 10],
         [inf, 0, 3, inf],
         [inf, inf, 0,   1],
         [inf, inf, inf, 0]]
print(FloydWarshall(graph))