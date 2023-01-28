def merge(T):
    if len(T)>1:
        r = len(T)//2
        L = T[:r]
        P = T[r:]

        merge(L)
        merge(P)

        i = j = k =0

        while i != len(L) and j != len(P):
            if L[i] < P[j]:
                T[k] = L[i]
                i+=1
            else:
                T[k] = P[i]
                j+=1
            k+=1

        while i != len(L):
            T[k] = L[i]
            i+=1
            k+=1

        while j != len(P):
            T[k] = P[j]
            j+=1
            k+=1
    return T

T=[19, 89, 34, 61, 38, 83, 83, 87, 92, 91, 82, 29, 8, 21, 62, 71, 4, 16, 66, 69, 51, 98, 15, 28, 41, 63, 88, 43, 31, 10]
print(merge(T))