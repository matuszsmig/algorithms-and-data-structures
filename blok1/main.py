def partition(tab,first,last):
    pivot = tab[last]
    i = first - 1
    for j in range(first,last):
        if tab[j] < pivot:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[last]=tab[last],tab[i+1]
    return i+1

def quicksort(tab, first, last):
    if first < last:
        pivot = partition(tab,first,last)
        quicksort(tab, first, pivot-1)
        quicksort(tab, pivot+1 , last)
    return tab

def mergesort(tab):
    if len(tab)>1:
        r = len(tab)//2
        L = tab[:r]
        P = tab[r:]

        mergesort(L)
        mergesort(P)

        i = j = k = 0
        while i < len(L) and j < len(P):
            if L[i] < P[j]:
                tab[k] = L[i]
                i+=1
            else:
                tab[k] = P[j]
                j+=1
            k+=1

        while i < len(L):
            tab[k] = L[i]
            i+=1
            k+=1

        while j < len(P):
            tab[k] = P[j]
            j+=1
            k+=1

    return tab

def wiadrosort(T):
    n = len(T)
    maxx = max(T)
    wynik = int(maxx)+1
    tablica = [[] for _ in range(wynik)]

    for i in range(n):
        tablica[int(T[i])].append(T[i])
    for i in range(wynik):
        tablica[i]=mergesort(tablica[i])
    k = 0
    for j in range(len(tablica)):
        for i in range(len(tablica[j])):
            tab[k]=tablica[j][i]
            k+=1
    return tab

#def counting_stars(tab):




tab = [5.5,4.3,8.2,9.1,3.7,2.9,6.2,2.4,2.11,2.94,1.3,7.5]
print(wiadrosort(tab))