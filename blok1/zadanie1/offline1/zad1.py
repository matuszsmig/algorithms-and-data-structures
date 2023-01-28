"""
Mateusz Śmigała
Mój algorytm jest to zmodyfikownay selection sort, który wyszukuje najmniejsze wartości w
przedziale [rozpatrywana liczba, rozpatrywana liczba+k] i wstawia go na koniec posortowanej dotychczas linked listy, a nastepnie
przeszkuje nieposortowaną część w poszukiwaniu następnego najmniejszego elementu. Rozpatruje osobny przypadek dla k = 1, ponieważ
sortowania można wówczas dokonać liniowo poprzez zamianę mniejszego elementu z większym, stojącym obok.
dla k = 1 algorytm ma złożoność czasową O(n) i wykonuje się liniowo
dla k = logn średnia zlożoność to O(nlogn), ponieważ przechodzi po elementach liniowo i wykonuje porównanie z k = logn elementów
dla k = n śrenią złożonościa jest O(n^2), ponieważ porównuje każdy z każdym element
"""

from zad1testy import Node, runtests


def SortH(p,k):
    g=Node()
    g.next = p
    toreturn = g
    if k == 1:
        while g.next.next:
            if g.next.val > g.next.next.val:
                tempnext = g.next.next.next
                temp = g.next
                g.next = g.next.next
                g.next.next = temp
                temp.next = tempnext
            g = g.next
    else:
        while g.next:
            prev = g
            curr = prev.next
            minn = curr
            licznik = 0
            flag = False
            if prev.val == curr.val:
                g = g.next
            else:
                while licznik <= k and curr is not None:
                    if curr.val < minn.val:
                        minn = curr
                        prevminn = prev
                        nextminn = minn.next
                        flag = True
                    prev = curr
                    curr = curr.next
                    licznik += 1
                if flag:
                    temp = g.next
                    g.next = minn
                    prevminn.next = nextminn
                    minn.next = temp
                g = g.next

    return toreturn.next


runtests( SortH ) 
