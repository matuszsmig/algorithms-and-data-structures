from zad6ktesty import runtests

def rek(S,i):
    n = len(S)
    if i == n:
        return 1
    counter = 0
    if i+1 < n and S[i+1]=="0":
        if int(S[i])<3:
            counter += rek(S, i + 2)
        else:
            return 0
    counter += rek(S,i+1)
    if int(S[i:i+2])<27:
        counter+=rek(S,i+2)
    return counter


def haslo ( S ):
    n = len(S)
    Dp =
    return rek(S,0)

runtests ( haslo )