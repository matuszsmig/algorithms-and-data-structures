from zad7ktesty import runtests

def podlej(T,i,j,x,y,Podlane):
    n = len(T)
    m = len(T[0])
    Podlane[i][j]=T[i][j]
    if j+1 < m and T[i][j+1]!=0 and Podlane[i][j+1] is None:
        T[x][y]+=T[i][j+1]
        Podlane[i][j + 1]=T[i][j+1]
        podlej(T, i, j+1, x, y,Podlane)
    if j -1 >= 0 and T[i][j-1]!=0 and Podlane[i][j-1] is None:
        T[x][y]+=T[i][j-1]
        Podlane[i][j - 1]=T[i][j-1]
        podlej(T, i, j-1, x, y,Podlane)
    if i + 1 < n and T[i+1][j]!=0 and Podlane[i+1][j] is None:
        T[x][y]+=T[i+1][j]
        Podlane[i+1][j]=T[i+1][j]
        podlej(T, i+1, j, x, y,Podlane)
    if i - 1 >= 0 and T[i-1][j]!=0 and Podlane[i-1][j] is None:
        T[x][y]+=T[i-1][j]
        Podlane[i-1][j]=T[i-1][j]
        podlej(T, i-1, j, x, y,Podlane)

def rek(Tprim, Z, l, i, DP):
    if DP[i][l] is not None:
        return DP[i][l]
    maxx = 0
    for j in range(i):
        if l-Tprim[j] > 0:
            maxx=max(maxx,rek(Tprim,Z,l-Tprim[j],j,DP)+Z[j])
    DP[i][l] = maxx
    return DP[i][l]

def ogrodnik (T, D, Z, l):
    n = len(T)
    m = len(T[0])
    N = len(D)
    Tprim = []
    Podlane = [[None for _ in range(m)]for _ in range(n)]
    for i in range(N):
        podlej(T, 0, D[i], 0, D[i], Podlane)
    for i in range(m):
        if T[0][i]!=0:
            Tprim.append(T[0][i])
    DP = [[None for _ in range(l+1)]for _ in range(N)]
    maxx = 0
    for i in range(N):
        maxx = max(maxx, rek(Tprim, Z, l, i,DP))
    return maxx

runtests( ogrodnik, all_tests=True )