def part(T,left,right):
    pivot = T[right]
    i = left-1
    for j in range(left,right):
        if T[j]<=pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[right],T[i+1]=T[i+1],T[right]
    return i+1

def kwiksort(T,left,right):
    if left<right:
        pivot = part(T,left,right)
        kwiksort(T,left,pivot-1)
        kwiksort(T,pivot+1,right)
    return T

def sprawdz(T):
    n = len(T)
    kwiksort(T,0,n-1)
    for iterator in range(n):
        wynik = T[iterator]
        i=0
        if i == iterator:
            i+=1
        j=n-1
        if j == iterator:
            j-=1
        while (T[i]+T[j])!=wynik and i!=j:
            if T[i]+T[j]>wynik:
                j-=1
                if j == iterator:
                    j-=1
            if T[i]+T[j]<wynik:
                i+=1
                if i == iterator:
                    i+=1
        if i == j:
            return False
    return True