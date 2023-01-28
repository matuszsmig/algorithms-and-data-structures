def merge(T):
    if len(T)>1:
        n = len(T)
        r = n//2
        L = T[:r]
        P = T[r:]
        merge(L)
        merge(P)

        i = j = k = 0
        while i!= len(L) and j!= len(P):
            if L[i] < P[j]:
                T[k]=L[i]
                i+=1
            else:
                T[k]=P[j]
                j+=1
            k+=1
        while i!= len(L):
            T[k]=L[i]
            i+=1
            k+=1
        while j!= len(P):
            T[k]=P[j]
            j+=1
            k+=1

    return T




def bucket(T):
    n = len(T)
    miejsca = 10
    tablica = [[]for i in range(miejsca)]

    for i in range(n):
        tablica[int(T[i]*miejsca)].append(T[i])
    for i in range(miejsca):
        merge(tablica[i])

    x = 0
    for i in range(len(tablica)):
        for j in range(len(tablica[i])):
            T[x]=tablica[i][j]
            x+=1
    return T

tab = [0.22,0.21,0.1,0.33,0.12,0.51,0.24,0.31,0.24]
print(bucket(tab))
