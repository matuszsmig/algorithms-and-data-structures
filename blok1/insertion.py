def insertion_sort(tab):
    n = len(tab)
    for i in range(1,n):
        j=i
        while j >= 1 and tab[j] < tab[j-1]:
            tab[j],tab[j-1]=tab[j-1],tab[j]
            j-=1
    return tab

tab = [5,4,8,9,3,2,6,1,7]

print(insertion_sort(tab))