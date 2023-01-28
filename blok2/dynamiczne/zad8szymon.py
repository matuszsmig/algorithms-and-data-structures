from zad8ktesty import runtests

def rek(s,t,slen,tlen,Tab):
    if Tab[tlen][slen] is not None:
        return Tab[tlen][slen]
    if slen == 0:
        return tlen
    if tlen == 0:
        return slen
    if s[slen-1]==t[tlen-1]:
        return rek(s,t,slen-1,tlen-1,Tab)
    minn = 999999999999999999999999999999999999
    minn = min(minn,1 + min(rek(s,t,slen-1,tlen,Tab),rek(s,t,slen-1,tlen-1,Tab),rek(s,t,slen,tlen-1,Tab)))
    Tab[tlen][slen]=minn
    return Tab[tlen][slen]

def napraw ( s, t ):
    slen = len(s)
    tlen = len(t)
    Tab = [[None for _ in range(slen+1)]for _ in range(tlen+1)]
    toret = rek(s, t, slen, tlen,Tab)
    return toret

runtests ( napraw )