def statek(T, i, n1, n2):
    if (T[i] > n1 and T[i] > n2) or i>len(T):
        return 0
    if T[i] > n1:
        statek(T, i + 1, n1, n2-T[i])+1
    if T[i] > n2:
        statek(T, i + 1, n1-T[i], n2)+1
    maxx = max(statek(T, i+1, n1-T[i],n2),statek(T, i+1, n1,n2-T[i]))+1
    return maxx

T = [2, 4, 3, 2, 1, 1, 4, 1, 2, 4,3, 5, 3, 2, 1]
print(statek(T,0,7,7))