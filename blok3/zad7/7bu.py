from zad7testy import runtests

def rek(G,tablica,Bramka,elem,itr):
    if itr == len(tablica) and (0 in G[Bramka][1] or 0 in G[Bramka][0]):
        print(":)")
        return True
    print(tablica,itr,len(tablica))
    if elem in G[Bramka][1]:
        gate = 0
    else:
        gate = 1
    tablica[itr]=Bramka
    for j in range(len(G[Bramka][gate])):
        if G[Bramka][gate][j] not in tablica[:itr]:
            rek(G,tablica,G[Bramka][gate][j],Bramka,itr+1)

def droga( G ):
    n = len(G)
    tablica = [0 for _ in range(n)]
    for i in range(len(G[0][0])):
        if rek(G,tablica,G[0][0][i],0,1):
            print(":)")
            break


    for i in range(n):
        if tablica[i] in tablica[i+1:]:
            return None
    return tablica

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( droga, all_tests = True )
G = [([1, 10, 11], [2, 3, 4]), ([0, 10, 11], [2, 5, 6]), ([1, 5, 6], [0, 3, 4]), ([0, 2, 4], [5, 7, 8]), ([0, 2, 3], [6, 7, 9]), ([1, 2, 6], [3, 7, 8]), ([1, 2, 5], [4, 7, 9]), ([4, 6, 9], [3, 5, 8]), ([3, 5, 7], [9, 10, 12]), ([4, 6, 7], [8, 10, 12]), ([0, 1, 11], [8, 9, 12]), ([0, 1, 10], [12]), ([11], [8, 9, 10])]
print(droga(G))
#       [0, 11, 12, 10, 1, 6, 9, 8, 7, 4, 3, 5, 2]