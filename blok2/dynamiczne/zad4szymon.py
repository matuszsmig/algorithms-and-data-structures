from zad4ktesty import runtests


def falisz ( T ):
    n = len(T)
    Tab = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(n):
        Tab[0][i] = Tab[0][i - 1]+T[0][i]
        Tab[i][0] = Tab[i - 1][0]+T[i][0]
    for i in range(1,n):
        for j in range(1,n):
            Tab[i][j]=min(Tab[i-1][j],Tab[i][j-1])+T[i][j]

    return Tab[n-1][n-1]

runtests ( falisz )