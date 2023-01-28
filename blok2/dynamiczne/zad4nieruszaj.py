from zad4testy import runtests

def studenci(T,i):
    wynik = (T[i][2]-T[i][1])*T[i][0]
    return wynik

def f(T, p ,k, i, Tab, prawy):
    #if Tab[i][k] > 0:
    #    return Tab[i][k]
    maxx = 0
    for j in range(k,i+1):
        if T[j][1] > prawy and p-T[j][3] > 0:
            maxx = max(maxx, f(T,p-T[j][3],j,i,Tab,T[j][2])+studenci(T,j))
    #Tab[i][k]=maxx
    return maxx

def select_buildings(T,p):
    T = sorted(T, key = lambda T: T[1])
    n = len(T)
    Tab = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    maxx = 0
    for j in range(n):
        maxx = max(maxx, f(T, p ,0,j,Tab,0))
    return maxx

runtests( select_buildings )

