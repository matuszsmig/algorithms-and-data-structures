def prityjnosc(liczba):
    tab = [0 for _ in range(10)]
    while liczba>0:
        if tab[liczba%10]<2:
            tab[liczba%10]+=1
        liczba//=10
    maxx = max(tab)
    if maxx==1:
        return 0
    sum = 0
    for i in range(len(tab)):
        if tab[i]==maxx:
            sum+=1
    return sum

def part(tab,left,right):
    pivot = prityjnosc(tab[right])
    i = left - 1
    for j in range(left,right):
        if prityjnosc(tab[j])<pivot:
            i+=1
            tab[i],tab[j]=tab[j],tab[i]
    tab[i+1],tab[right]=tab[right],tab[i+1]
    return i+1

def quicksort(T,left,right):
    if left<right:
        pivot = part(T,left,right)
        quicksort(T, left, pivot-1)
        quicksort(T, pivot + 1, right)
    return T

tablica = [1122,1,1122334444,44,22,123,111,666111,222333444]
print(quicksort(tablica,0,len(tablica)-1))