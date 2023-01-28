"""
Mateusz Śmigała
Algorytm ma złożoność O(n), ze względu na sortowanie kubełkowe, dodatkowo używam insertion sorta, do sortowania
elementów w obrębi kubełka, ilość kubeczków jest dobrana na podstawie metody prób i błędów, tak aby algorytm
działał jak najszybciej.
"""

from zad3testy import runtests

def insertion_sort(tab):
    n = len(tab)
    for i in range(1,n):
        j=i
        while j >= 1 and tab[j] < tab[j-1]:
            tab[j],tab[j-1]=tab[j-1],tab[j]
            j-=1
    return tab

def SortTab(T,P):
    maxx = max(T)
    minn = min(T)
    numOfBuckets = int(len(T)//7.07)+1

    rng = (maxx - minn) / numOfBuckets
    array = []
    for i in range(numOfBuckets):
        array.append([])
    for i in range(len(T)):
        diff = (T[i] - minn) / rng - int((T[i] - minn) / rng)

        if (diff == 0 and T[i] != minn):
            array[int((T[i] - minn) / rng) - 1].append(T[i])

        else:
            array[int((T[i] - minn) / rng)].append(T[i])
    for i in range(len(array)):
        if len(array[i])!=0:
            array[i]=insertion_sort(array[i])

    k=0
    for i in array:
        if i:
            for j in i:
                T[k] = j
                k+=1
    return T

runtests( SortTab )