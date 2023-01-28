def part(T,first,last):
    pivot = T[last]
    i = first-1
    for j in range(first,last):
        if T[j]<=pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[last]=T[last],T[i+1]
    return i+1

def quickselcet(T,first,last,number):
    index = part(T,first,last)
    if index-first==number-1:
        return T[index]
    if index - first > number - 1:
        return quickselcet(T,first,index-1,number)
    return quickselcet(T,index+1,last,number-index+first-1)

def quicksort(T,first,last):
    if first<last:
        pivot = part(T,first,last)
        quicksort(T,first,pivot-1)
        quicksort(T,pivot+1,last)

def section(T,p,q):

    quickselcet(T,0,len(T)-1,q)
    quicksort(T, 0, q+1)
    return T[p:q+1]

T = [1.88,1.22,1.90,1.55,1.234,1.98,1.99,2.00,1.80,1.81,1.32,1.01,1.85,1.54,2.11,1.92,1.54]

print(section(T,3,7))
print(T)
T.sort()
print(T)
