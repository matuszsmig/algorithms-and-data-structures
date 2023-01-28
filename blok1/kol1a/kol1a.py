from kol1atesty import runtests
"""
Mateusz Śmigała
Złożoność czasowa mojego algorytmu to O(NlogN) ze względu na dwie pętle w funkcji g(T), natomiat zlożoność pamięciowa jest 
to O(N) ze wszględu na tablice "kubelki" ktora jest dlugosci N. Algorytm się zaczyna od posortowania bucketsortem 
wyrazów z T, pod względem dlugości, następnie dwoma pętlami wyznaczam długość najsilniejszego wyrazu, używając
przy tym funkcji reverse odwracającą napis.
Aby usprawnić działanie algorytmu możnaby zrobić tablice posortowaną pod długościu wyrazu, z wyrazami nie powtarzającymi
się, tak by pętle sie nie wykonywały tak wiele razy, byłby to swego rodzaju bucketsort+countingsort
"""

def rozdzielDoKubelkow(T):
    #szukam najdluzszego napisu aby stworzyc kubeczki
    maxx=0
    for i in range(len(T)):
        if len(T[i])>maxx:
            maxx=len(T[i])
    kubki = [[] for _ in range(maxx)]
    for i in range(len(T)):
        kubki[len(T[i])-1].append(T[i])
    k = 0
    for i in range(len(kubki)):
        for j in range(len(kubki[i])):
            T[k]=kubki[i][j]
            k+=1

    return T

def reverse(napis):
    #odwracam napis
    napistoreturn = napis[::-1]
    return napistoreturn


def g(T):
    kubki = rozdzielDoKubelkow(T) # bucketsort zlozonosc O(k), k dlugosc najdluzszego napisu
    n = len(kubki)
    maxx=0
    for i in range(n):
        odp = 1   # odpowiedz ustawiona na jeden, po to by jesli znajdziemy jakies slowo rownowazne do danego, dane slowo rowniez
        flag=False                            # zostalo zliczone
        for j in range(i+1,n):
            if len(kubki[i])!=len(kubki[j]): #petla wykonuje sie logN razy,to znaczy dopki dlugosc wyrazu kubki[i] jest taka
                break                        #sama jak dlugosc wyrazu kubki[j]
            if reverse(kubki[i])==kubki[j] or kubki[i]==kubki[j]:
                flag = True                   #po to aby maxx byl 0 jesli petla nie znajdzie wyrazow "rownowaznych"
                odp+=1
        if odp>maxx and flag:
            maxx=odp

    return maxx


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )