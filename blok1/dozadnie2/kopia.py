from zad2testy import runtests


def partitnion(T, first,last):
    last_item = T[last][0]
    i = first-1
    for j in range(first,last):
        if T[j][0]<=last_item:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[last]=T[last],T[i+1]
    return i+1

def quicksort(T,first,last):
    if first<last:
        pivot = partitnion(T, first, last)
        quicksort(T, first, pivot - 1)
        quicksort(T,pivot+1,last)

def swap2nd(T):
    maxx = 0
    ind = 0
    for i in range(len(T)):
        if T[i][1]>maxx and T[i][0]==T[ind][0]:
            maxx=T[i][1]
            T[i],T[ind] = T[ind],T[i]
        if T[i][0]!=T[ind][0]:
            maxx=T[i][1]
            ind = i
    return T

def depth(L):
    quicksort(L, 0, len(L) - 1)
    swap2nd(L)
    maxx=0
    n = len(L)
    i=0
    right = L[i][1]
    left = L[i][0]
    for j in range(1,n):
        if L[j][1]<=right:
            maxx+=1
        else:
            i+=1
        if left!=L[i][0] and L[i][1]>right:
            left=L[i][0]
            right=L[i][1]
    return maxx


runtests( depth )