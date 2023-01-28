import time
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
    odejmij = 0
    wartosc = L[0][1]
    for j in range(1, n):
        if odejmij>maxx:
            maxx=odejmij
            odejmij=0
            i=j-odejmij
            wartosc=L[i][1]
        if L[j][1]<=wartosc:
            maxx+=1
            odejmij=-1
        else:
            odejmij+=1
    return maxx

T=[[1,124],[1,91],[2,213],[2,210],[2,190],[3,91],[4,54]]
#print(depth(T))
#quicksort(T,0,len(T)-1)
#print(T)
#swap2nd(T)
print(time.process_time())
#print(T)
print(depth(T))