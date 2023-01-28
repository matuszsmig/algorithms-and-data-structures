from zad8testy import runtests

def leng(A,i,j):
    odp = int(((A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2)**(1/2))+1
    return odp

def highway( A ):
    minn = 99999999999999999999999999999999999999
    n = len(A)
    T = []
    for i in range(n):
        for j in range(i+1,n):
            T.append(((leng(A,i,j)),i,j))
    N = len(T)
    T.sort()
    print(T)
    return minn

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( highway, all_tests = False )
A = [(10, 10), (15, 25), (20, 20), (30, 40)]
print(highway(A))