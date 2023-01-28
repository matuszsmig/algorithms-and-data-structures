from zad7testy import runtests

"""
Mateusz Śmigała
W moim programie obieram sobie punkt z którego startuje, a następnie w rekurencji sprawdza z której bramy weszliśmy i 
analizuje bramy którymi powinniśmy wyjść, jeśli znajdzie takie ścieżkę by odwiedzić wszytkie miasta zwraca daną ścieżkę,
w przeciwnym przypadku zwraca None.
"""

def rek(G,tablica,Bramka,elem,itr):
    n = len(tablica)
    if elem in G[Bramka][1]:
        gate = 0
    else:
        gate = 1
    tablica[itr] = Bramka
    if itr == n-1 and 0 in G[Bramka][gate]:
        return True
    for j in range(len(G[Bramka][gate])):
        if G[Bramka][gate][j] not in tablica[:itr]:
            if rek(G,tablica,G[Bramka][gate][j],Bramka,itr+1):
                return True
    return False

def droga( G ):
    n = len(G)
    tablica = [0 for _ in range(n)]
    for i in range(len(G[0][0])):
        if rek(G,tablica,G[0][0][i],0,1):
            break
    for i in range(n):
        if tablica[i] in tablica[i+1:]:
            return None
    return tablica

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )