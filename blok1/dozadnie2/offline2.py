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
    print(L)
    maxx=0
    n = len(L)
    pivot = L[0]
    counter = 0
    itr = 0
    i = 1
    while i < n:
        flag = True
        while L[itr][0]<=pivot[1]:
            if L[itr][1]<=pivot[1]:
                counter+=1
            itr+=1
        if counter > maxx:
            maxx = counter
            counter=0
        i+=1
        #pivot=L[next]


    return maxx




T=[[1, 14], [2, 77], [2, 53], [3, 8], [4, 55], [6, 93], [6, 85], [6, 81], [6, 41], [6, 53], [6, 45], [6, 81], [7, 64], [7, 52], [9, 58], [9, 38], [9, 14], [10, 81], [10, 29], [20, 55], [22, 85], [23, 72], [24, 79], [27, 76], [28, 31], [30, 41], [31, 72], [34, 37], [35, 88], [35, 60], [36, 71], [36, 67], [38, 77], [41, 42], [43, 72], [43, 64], [47, 84], [49, 58], [51, 56], [52, 75], [53, 58], [56, 99], [56, 67], [60, 91], [61, 98], [61, 82], [71, 80], [72, 79], [80, 87], [82, 97]]
print(time.process_time())
print(depth(T))