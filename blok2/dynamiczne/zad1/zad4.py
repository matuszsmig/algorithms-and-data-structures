"""
Mateusz Śmigała
Mój algorytm nie jest algorytmem dynamicznym, jest to rekurencja bez spamiętywania, króra dodaje do tablicy
j-ty akademik o ile ten nie przekraczacza pozostałego budżetu i rozpatruje kandydata do dodania do tablicy, o ile
ten nie nachodzi na inne budynki i w taki sposób szukam akademików mogących pomieścić jak najwięcej studentów.
"""

from zad4testy import runtests

def rekurencja(T, n, i, p, obecne_ust, najlepsze_ust = []):
    if i == n:
        sum1, sum2 = 0, 0
        for el in obecne_ust:
            sum1 += T[el][0] * (T[el][2] - T[el][1])
        for el in najlepsze_ust:
            sum2 += T[el][0] * (T[el][2] - T[el][1])
        if sum1 > sum2:
            return obecne_ust
        return najlepsze_ust
    for j in range(i, n):
        if T[j][3] < p:
            flag = 1
            for el in obecne_ust:
                if not (T[j][1] > T[el][2] or T[j][2] < T[el][1]):
                    flag = 0
                    break
            if flag == 1:
                najlepsze_ust = rekurencja(T, n, j + 1, p - T[j][3], obecne_ust + [j], najlepsze_ust)
        if j == n-1:
            sum1, sum2 = 0, 0
            for el in obecne_ust:
                sum1 += T[el][0] * (T[el][2] - T[el][1])
            for el in najlepsze_ust:
                sum2 += T[el][0] * (T[el][2] - T[el][1])
            if sum1 > sum2:
                return obecne_ust
            return najlepsze_ust
    return najlepsze_ust

def select_buildings(T,p):
    n = len(T)
    tab = []
    ans_tab = rekurencja(T, n, 0, p, tab)
    return ans_tab

runtests( select_buildings )