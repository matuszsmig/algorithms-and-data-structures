def pociecie(T, N, i, odp,ans):
    if N==0:
        if odp>ans[0]:
            ans[0]=odp
        return
    if N < 0 or i==len(T):
        return 0
    pociecie(T, N, i+1, odp,ans)
    pociecie(T,N-i-1,i+1,odp+T[i],ans)
    pociecie(T, N - i - 1, i, odp + T[i],ans)


ans = [0]
N = 8
P = [1, 5, 8, 9, 10, 17, 17, 20]
pociecie(P,N,0,0,ans)
print(ans[0])