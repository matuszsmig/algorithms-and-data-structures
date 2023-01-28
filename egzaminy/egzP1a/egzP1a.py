from egzP1atesty import runtests

#dynamik

def mergesort(T):
    if len(T)>1:
        r = len(T)//2
        L = T[:r]
        M = T[r:]

        mergesort(L)
        mergesort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if len(L[i][1])<len(M[j][1]):
                T[k]=L[i]
                i+=1
            else:
                T[k]=M[j]
                j+=1
            k+=1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            T[k] = M[j]
            j += 1
            k += 1

    return T

def titanic( W, M, D ):

    #print(W)
    #print(D)

    napis = ""
    for i in range(len(W)):
        napis += M[(ord(W[i])-65)][1]

    litery = []
    for i in range(len(D)):
        litery.append(M[D[i]])

    mergesort(litery)
    litery.reverse()

    licznik = 0
    left = 0

    print(napis)
    print(litery)
    napis2 = ""

    while left!=len(napis):
        for i in range(len(litery)):
            if litery[i][1]==napis[left:left+len(litery[i][1])]:
                licznik+=1
                left+=len(litery[i][1])
                napis2+=litery[i][0]
                napis2+=" "
                break

    print(napis2)
    return licznik

runtests ( titanic, recursion=False )