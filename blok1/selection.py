def searchmin(tab):
    minn = 0
    j=0
    for i in range(len(tab)):
        if tab[i]<minn or minn ==0:
            minn=tab[i]
            j=i
    return j


def selection_sort(tab):
    n = len(tab)
    for i in range(n):
        minn=searchmin(tab[i:])+i
        tab[i],tab[minn]=tab[minn],tab[i]
        print(tab)
    return tab

tab = [5,4,8,9,3,2,6,1,7]

print(selection_sort(tab))