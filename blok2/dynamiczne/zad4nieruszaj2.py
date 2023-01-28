from zad4testy import runtests

def studenci(T,i):
    wynik = (T[i][2]-T[i][1])*T[i][0]
    return wynik

def f(T, p, i, prawy, Tab):
    #if Tab[p][i] > 0:
    #    return Tab[p][i]
    maxx = 0
    for j in range(i+1):
        if T[j][1] > prawy and p-T[j][3] >= 0:
            maxx = max(maxx, f(T, p-T[j][3], j, T[j][2], Tab)+studenci(T,j))
    #Tab[p][i]=maxx
    return maxx

def select_buildings(T,p):
    T = sorted(T, key = lambda T: T[1])
    n = len(T)
    Tab = [[-1 for _ in range(n+1)] for _ in range(p+1)]
    maxx = 0
    for j in range(n):
        maxx = max(maxx, f(T, p,j,0,Tab))
    #for i in range(n+1):
    #    print(Tab[i])
    return maxx

runtests( select_buildings )
T = [(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3), (4, 5, 6, 7), (3, 1, 3, 19), (2, 19, 20, 3), (3, 8, 10, 3), (3, 11, 12, 3)]
p = 20
#print(select_buildings(T, p))