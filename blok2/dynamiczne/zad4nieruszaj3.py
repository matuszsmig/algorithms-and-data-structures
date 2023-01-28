from zad4testy import runtests

def studenci(T,i):
    wynik = (T[i][2]-T[i][1])*T[i][0]
    return wynik

def f(T, p ,k, i, Tab, prawy):
    if Tab[i][k] is not None:
        return Tab[i][k]
    maxx = 0
    for j in range(k,i+1):
        if T[j][1] > prawy and p-T[j][3] >= 0:
            maxx = max(maxx, f(T,p-T[j][3], j, i, Tab, T[j][2])+studenci(T,j))
    Tab[i][k]=maxx
    return Tab[i][k]

def select_buildings(T,p):
    n = len(T)
    T2 = T
    T = sorted(T, key = lambda T: T[1])
    T3 = []
    for i in range(n):
        T3.append(T2.index(T[i]))
    Tab = [[None for _ in range(n+1)] for _ in range(n+1)]
    maxx = 0
    jmax = 0
    for j in range(n):
        temp = f(T, p ,0,j,Tab,0)
        if temp>maxx:
            maxx = temp
            jmax = j
    print(T3[jmax])
    return maxx

runtests( select_buildings )
P = [(5, 3, 4, 15), (4, 1, 11, 11), (3, 1, 6, 7), (2, 1, 7, 3), (3, 4, 7, 19), (4, 15, 28, 7), (3, 1, 2, 7), (4, 7, 14, 19), (3, 8, 22, 15), (4, 13, 17, 3), (3, 12, 14, 15), (4, 23, 34, 15), (3, 20, 23, 3), (4, 13, 15, 15), (3, 8, 14, 11), (2, 23, 26, 19), (3, 16, 29, 11), (4, 27, 32, 15), (3, 28, 30, 19), (4, 19, 36, 11), (3, 18, 22, 19), (3, 33, 46, 7), (4, 28, 35, 3), (3, 25, 27, 7), (2, 30, 32, 11), (3, 23, 31, 11), (2, 32, 38, 11), (3, 29, 38, 11), (4, 22, 26, 15), (3, 35, 45, 15), (4, 24, 25, 3), (3, 33, 35, 3), (2, 30, 32, 19), (3, 31, 47, 7), (4, 34, 38, 11), (3, 43, 52, 3), (2, 34, 36, 3), (3, 35, 37, 3), (3, 36, 39, 19), (2, 25, 28, 7), (3, 44, 45, 3), (3, 41, 42, 19), (3, 60, 71, 19), (4, 35, 39, 11), (3, 48, 58, 7), (4, 51, 52, 15), (3, 38, 46, 7), (4, 43, 50, 3), (3, 50, 51, 11), (4, 41, 45, 7), (3, 50, 53, 15), (3, 37, 39, 3), (3, 52, 55, 11), (3, 43, 46, 3), (2, 56, 59, 3), (3, 55, 58, 15), (3, 44, 57, 15), (2, 69, 82, 19), (3, 68, 84, 15), (3, 63, 67, 11), (2, 70, 76, 15), (3, 75, 90, 11), (2, 60, 69, 15), (3, 69, 78, 7), (2, 64, 66, 11), (3, 69, 71, 7), (3, 70, 74, 19), (4, 51, 59, 7), (3, 62, 64, 15), (4, 67, 78, 11), (3, 62, 63, 19), (3, 75, 76, 11), (3, 70, 79, 3), (3, 71, 74, 7), (4, 80, 85, 3), (3, 73, 75, 7), (4, 70, 73, 19), (3, 69, 77, 19), (4, 62, 80, 15), (3, 87, 96, 11), (3, 90, 92, 19), (3, 83, 92, 7), (2, 86, 92, 7), (3, 77, 81, 3), (3, 84, 86, 15), (3, 71, 76, 3), (2, 88, 89, 3), (3, 87, 90, 3), (2, 86, 89, 15), (3, 103, 111, 3), (3, 88, 91, 7), (2, 95, 97, 7), (3, 96, 102, 11), (4, 97, 100, 7), (3, 98, 103, 3), (2, 93, 96, 11), (3, 92, 99, 3), (2, 95, 98, 7), (3, 96, 102, 7), (3, 105, 107, 7)]