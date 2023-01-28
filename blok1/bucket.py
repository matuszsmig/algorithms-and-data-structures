def mergesort(T):
    if len(T)>1:
        r = len(T)//2
        L = T[:r]
        M = T[r:]
        mergesort(L)
        mergesort(M)
        i = j = k = 0
        while i < len(L) and j < len(M):
            if L[i]<M[j]:
                T[k]=L[i]
                i+=1
            else:
                T[k]=M[j]
                j+=1
            k+=1
        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            T[k] = M[j]
            j += 1
            k += 1
    return T

def bucketsort(tab):
    tablica = []
    n = len(tab)
    slot = 10

    for i in range(slot):
        tablica.append([])

    for j in tab:
        index = int(slot*j)
        tablica[index].append(j)

    for i in range(slot):
        tablica[i] = mergesort(tablica[i])

    k = 0
    for i in range(slot):
        for j in range(len(tablica[i])):
            tab[k] = tablica[i][j]
            k+=1
    return tab


tab = [0.12, 0.55, 0.33, 0.78, 0.22, 0.99,0.11]
print(bucketsort(tab))