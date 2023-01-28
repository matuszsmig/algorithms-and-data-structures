def bubble_sort(tab):
    n = len(tab)
    while n != 1:
        for i in range(n-1):
            if tab[i]>tab[i+1]:
                tab[i],tab[i+1]=tab[i+1],tab[i]
        n-=1
    return tab

tab = [5,4,8,9,3,2,6,1,7]

print(bubble_sort(tab = [5,4,8,9,3,2,6,1,7]))