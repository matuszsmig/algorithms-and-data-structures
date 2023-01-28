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

tab = [5,4,8,9,3,2,6,1,7]
print(mergesort(tab))