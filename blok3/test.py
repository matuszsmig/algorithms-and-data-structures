def partition(T,left,right):
    pivot = T[right]
    i = left - 1
    for j in range(left,right):
        if T[j]<=pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[right]=T[right],T[i+1]
    return i+1


def quicksort(T,left,right):
    if left<right:
        pivot = partition(T,left,right)
        quicksort(T, left, pivot-1)
        quicksort(T, pivot + 1, right)
    return T

T = ["abd","dbca","abcde"]
print(quicksort(T,0,len(T)-1))



print(T[0]>T[1])