class Node:
   def __init__(self, val, next=None):
      self.val = val
      self.next = next

def print_Node(first):
    while first is not None:
        print(" ->",first.val,end="")
        first=first.next

def make_linked_list(tab):
    first = None
    n = len(tab)
    for i in range(n-1,-1,-1):
        temp = Node(tab[i])
        temp.next = first
        first = temp
    return first

def findmid(first):
    if first is None:
        return None
    if first.next is None:
        return first

    left = first
    right = first
    while right.next is not None and right.next.next is not None:
        left=left.next
        right=right.next.next
    return left

def merge(L, P):
    list = Node(None)
    toreturn = list

    if L is None:
        return P
    if P is None:
        return L
    #print(P.val,L.val)
    while L.next is not None and P.next is not None:
        if L.val < P.val:
            list.next = L
            L=L.next
            print(L.val)
        else:
            list.next = P
            P = L.next
            print(P.val)
        list = list.next
        print(list.val)
    while L.next is not None:
        list.next = L
        list=list.next
        L=L.next
        print(L.val)
    while P.next is not None:
        list.next = P
        list=list.next
        P=P.next
        print(P.val)
    print()
    return toreturn.next

def mergeSort(first):
    if first is None:
        return None
    if first.next is None:
        return first

    mid = findmid(first)
    midn = mid.next
    mid.next=None

    L = mergeSort(first)
    P = mergeSort(midn)
    print_Node(L)

    toreturn = merge(L,P)
    return toreturn

tablica = [1.23,5.1234,2.22,8.1,3.81,7.22,0.2,9.2213,9.22,9.1,1.09]
tablica=make_linked_list(tablica)
first = mergeSort(tablica)
print_Node(first)