from zad6testy import runtests
from collections import deque
"""
Mateusz Śmigała
Moje podejście polega na wykonaniu BFSa i znaleznieniu najkrótszej ścieżki z wierchołka s do t. Następnie za pomocą
rodziców odczytuje daną najkótszą ścieżke. W kolejnym kroku szukam najkótszej ścieżki "usuwając" z grafu wierchołki
parami należące do wcześniej odczytanej najkrótszej ścieżki, jeżeli po usunięciu pary wierzchołków najkrótsza ścieżka
zmieni swoją długość zwracam dane wierzchołki.
"""
def BFS(G, p):
    Visited = [False for _ in range(len(G))]
    Distance = [0 for _ in range(len(G))]
    Parents = [[] for _ in range(len(G))]
    Que = deque()
    Que.append(p)
    Visited[p] = True
    while Que:
        u = Que.popleft()
        for v in G[u]:
            if Visited[v] is False:
                Visited[v] = True
                Distance[v]=Distance[u]+1
                Parents[v].append(u)
                Que.append(v)
    return (Distance,Parents)

def BFS2(G, s ,p ,q):
    Visited = [False for _ in range(len(G))]
    Distance = [0 for _ in range(len(G))]
    Que = deque()
    Que.append(s)
    Visited[s] = True
    while Que:
        u = Que.popleft()
        for v in G[u]:
            if u!=p or v!=q:
                if Visited[v] is False:
                    Visited[v] = True
                    Distance[v]=Distance[u]+1
                    Que.append(v)
    return Distance

def longer( G, s, t ):
    tabs = BFS(G,s)
    ansS = tabs[0]
    parS = tabs[1]
    odpS = parS[t][0]
    parentsS=[odpS]
    while odpS:
        sol = odpS
        odpS = parS[sol][0]
        parentsS.append(odpS)
    parentsS.reverse()
    parentsS.append(t)
    odp = ansS[t]
    for i in range(len(parentsS)-1):
        tablica = BFS2(G,s,parentsS[i],parentsS[i+1])
        odp2=tablica[t]
        if odp2!=odp:
            return (parentsS[i],parentsS[i+1])
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )