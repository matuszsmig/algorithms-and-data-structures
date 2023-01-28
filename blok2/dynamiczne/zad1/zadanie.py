from zad4testy import runtests

def studenci(T,i):
    wynik = (T[i][2]-T[i][1])*T[i][0]
    return wynik

def f(T, p, i, prawy, Tab):
    if Tab[p][i][0] > 0:
        return Tab[p][i]
    maxx = 0
    pmax=p
    imax = i
    for j in range(i+1):
        if T[j][1] > prawy and p-T[j][3] >= 0:
            temp = f(T, p-T[j][3], j, T[j][2], Tab)[0] +studenci(T,j)
            if maxx<temp:
                maxx = temp
                imax=j
                pmax=p-T[j][3]
                Tab[p][i] = [maxx, Tab[pmax][imax][1]]
                if T[i][4] not in Tab[p][i][1]:
                    Tab[p][i][1].append(T[i][4])

    return Tab[p][i]

def select_buildings(T,p):
    for i in range(len(T)):
        T[i]=(T[i][0],T[i][1],T[i][2],T[i][3],i)
    T = sorted(T, key = lambda T: T[1])
    n = len(T)
    Tab = [[[-1,[]] for _ in range(n)] for _ in range(p+1)]
    maxx = 0
    Back = []
    for j in range(n):
        temp = f(T, p,j,0,Tab)[0]
        if temp > maxx:
            maxx = temp
            Back = f(T, p,j,0,Tab)[1]
    print(maxx)
    return Back

runtests( select_buildings )
T = [(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3), (4, 5, 6, 7), (3, 1, 3, 19), (2, 19, 20, 3), (3, 8, 10, 3), (3, 11, 12, 3)]
p = 20
#print(select_buildings(T, p))