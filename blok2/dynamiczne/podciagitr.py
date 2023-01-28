def f(T):
    n = len(T)
    tab = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            #if i==0 or j == 0:
            #    tab[i][j] = 0
            #else:
            if T[j-1] > T[i-1]:
                tab[i][j]=max(tab[i][j-1],tab[i-1][j-1],tab[i-1][j])+1
            else:
                tab[i][j]=max(tab[i][j-1],tab[i-1][j-1],tab[i-1][j])
    for i in range(n+1):
        print(tab[i])


T = [4,5,1,3,2,6,8,4,5,7]
print(f(T))