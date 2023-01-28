def partitnion(T,first,last):
    x=T[last]
    i = first-1
    for j in range(first,last):
        if T[j]<=x:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[last]= T[last],T[i+1]
    return i+1

def quicksort(T,first,last):
    if first<last:
        q = partitnion(T,first,last)
        quicksort(T,first,q-1)
        quicksort(T,q+1,last)


T=[7,1,9,4,5,2,6,3]
quicksort(T,0,len(T)-1)
print(T)