def rekurencja(T,i,j,przypadki,ans):
    if j < 0:
        if przypadki not in ans:
            ans.append(przypadki)
        return
    if T[j]<T[i]:
        rekurencja(T,j,j-1,przypadki+1,ans)
    rekurencja(T, i, j - 1, przypadki,ans)

def main(T):
    n = len(T)
    ans=[]
    rekurencja(T,n-1,n-2,1,ans)
    odp = max(ans)
    return odp

T = [4,5,1,3,2,6,8,4,5,7]
print(main(T))