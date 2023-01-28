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

def selectionSort(p,k):
    g=Node(None)
    g.next = p
    toreturn = g
    while g.next.next:
        if g.next.val>g.next.next.val:
            tempnext = g.next.next.next
            temp = g.next
            g.next=g.next.next
            g.next.next=temp
            temp.next=tempnext
        g=g.next

    return toreturn.next


tab = [2, 6, 6,6,6,6,6, 10, 29, 24, 31, 43, 36, 45, 51, 49, 52, 56, 53, 56, 61, 58, 71, 75, 72, 79, 93, 82, 99]
first1 = make_linked_list(tab)
first2 = selectionSort(first1,1)
print_Node(first2)