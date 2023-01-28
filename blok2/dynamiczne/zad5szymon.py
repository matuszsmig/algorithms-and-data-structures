from zad5ktesty import runtests

def rek(A,i,j,Tab):
    if Tab[i][j] is not None:
        return Tab[i][j]
    if j <= i:
        return 0
    maxx = max(min(rek(A,i+2,j,Tab)+A[i],rek(A,i+1,j-1,Tab)+A[i]),min(rek(A,i,j-2,Tab)+A[j],rek(A,i+1,j-1,Tab)+A[j]))
    Tab[i][j]=maxx
    return Tab[i][j]

def garek ( A ):
    n = len(A)
    Tab = [[None for _ in range(n+1)]for _ in range(n+1)]
    maxx = 0
    j = n-1
    for i in range(n):
        maxx = max(maxx,rek(A,i,j,Tab))
    return maxx

runtests ( garek )