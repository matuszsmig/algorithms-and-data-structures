from zad12ktesty import runtests

def sum(T,j,i,Tablica):
    if Tablica[j][i] is not None:
        return Tablica[j][i]
    suma = 0
    for k in range(j,i):
        suma+=T[k]
    Tablica[j][i]=suma
    return suma

def rek(T,k,i,Tablica,Tablica2):
    if Tablica2[i][k] is not None:
        return Tablica2[i][k]
    minn = 9999999999999999999999
    if k == 0:
        return sum(T,0,i,Tablica)
    for j in range(i):
        minn = min(minn, max(rek(T,k-1,j,Tablica,Tablica2),sum(T,j,i,Tablica)))
    Tablica2[i][k] = minn
    return minn

def autostrada( T, k ):
    n = len(T)
    Tablica = [[None for _ in range(n+2)] for _ in range(n+2)]
    Tablica2= [[None for _ in range(k+1)]for _ in range(n+1)]
    minn = rek(T,k-1,n,Tablica,Tablica2)
    return minn

runtests ( autostrada,all_tests=True )
#T = [5, 10, 30, 20, 15]
#k = 3
#print(autostrada(T,k))