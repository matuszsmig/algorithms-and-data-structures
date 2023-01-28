def cutRod(T,N):
    t = [[0 for i in range(N+1)] for j in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if i==0 or j == 0:
                t[i][j]=0
            elif i<=j:
                t[i][j]=max((T[i-1]+t[i][j-i]),(t[i-1][j]))
            else:
                t[i][j]=t[i-1][j]
    return t[N][N]

N = 8
P = [1,5,8,9,10,17,17,20]
print(cutRod(P,N))