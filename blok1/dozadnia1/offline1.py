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




tab = [85, 58, 31, 28, 47, 98, 9, 35, 8, 30, 36, 41, 10, 61, 6, 81, 53, 76, 67, 58, 81, 84, 3, 88, 27]
first1 = make_linked_list(tab)
first2 = selectionSort(first1,25)
print_Node(first2)