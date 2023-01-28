from zad11ktesty import runtests

def rek(T,i,wartosc,Tab):
    if i == len(T):
        return wartosc
    if Tab[abs(wartosc)][i] is not None:
        return Tab[abs(wartosc)][i]
    minn = 9999999999999999999999999999999
    v1 = rek(T,i+1,wartosc+T[i],Tab)
    v2 = rek(T,i+1,wartosc-T[i],Tab)
    minn = min(minn, abs(v1),abs(v2))
    Tab[abs(wartosc)][i]=minn
    return minn


def kontenerowiec(T):
    n = len(T)
    T.sort()
    suma = 0
    for i in range(n):
        suma+=T[i]
    Tab = [[None for _ in range(n)]for _ in range(suma+2)]
    minn = rek(T,0,0,Tab)

    return minn

runtests ( kontenerowiec )