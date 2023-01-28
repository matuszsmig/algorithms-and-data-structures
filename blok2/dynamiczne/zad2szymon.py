from zad2ktesty import runtests

def palindrom( S ):
    n = len(S)
    if n < 2:
        return n
    start = 0
    maxLen = 1
    for i in range(n):
        left = i-1
        right = i+1
        while right < n and S[right]==S[i]:
            right +=1
        while left >= 0 and S[left]==S[i]:
            left-=1
        while left >=0 and right < n and S[left]==S[right]:
            left-=1
            right+=1
        lenght = right-left-1
        if lenght > maxLen:
            maxLen=lenght
            start=left+1
    return S[start:start+maxLen]

runtests ( palindrom )