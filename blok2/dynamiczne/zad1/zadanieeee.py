from zad4testy import runtests

def studenci(T,i):
    wynik = (T[i][2]-T[i][1])*T[i][0]
    return wynik

def f(T, p ,k, i, Tab, prawy, Back):
    if Tab[p][i][k] > 0:
        return Tab[p][i][k]
    maxx = 0
    for j in range(k,i+1):
        if T[j][1] > prawy and p-T[j][3] > 0:
            temp = f(T,p-T[j][3],j,i,Tab,T[j][2], Back)+studenci(T,j)
            if temp >= maxx:
                maxx = temp
                Back[p][i][k]=[p, i , j, p]
    Tab[p][i][k]=maxx
    return Tab[p][i][k]

def select_buildings(T,p):
    T = sorted(T, key = lambda T: T[1])
    n = len(T)
    Tab = [[[-1 for _ in range(n+1)] for _ in range(n+1)] for _ in range(p+1)]
    Back = [[[-1 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(p + 1)]
    res = []
    maxx = 0
    for j in range(n):
        temp = f(T, p ,0,j,Tab,0,Back)
        if temp>maxx:
            maxx=temp
            print(Back[j])
            #Back[p][j][0]
    return maxx

runtests( select_buildings )

