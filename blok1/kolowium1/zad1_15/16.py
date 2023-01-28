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

def select(first):
    g=Node(None)
    g.next=first
    toretrun = g
    while g.next is not None:
        cp = g
        maxx = 0
        while cp.next is not None:
            if cp.next.val > maxx:
                temp = cp
                maxx=cp.next.val
            cp=cp.next
        nextoftemp = temp.next.next
        wstaw = temp.next
        temp.next=nextoftemp
        nextt=g.next
        g.next=wstaw
        g.next.next=nextt
        g=g.next

    return toretrun.next

def zadanie(first):
    g = Node(None)
    g.next = first
    head = [None for _ in range(10)]
    tail = [Node(None) for _ in range(10)]
    for i in range(len(head)):
        head[i]=tail[i]
    while g.next is not None:

        zmienna=g.next
        b = 9 - int(zmienna.val)
        temp = zmienna.next
        zmienna.next=None

        tail[b].next = zmienna
        tail[b] = tail[b].next
        g.next=temp

    for i in range(len(head)):
        if head[i] is not None:
            head[i]=select(head[i].next)

    finallist = Node(None)
    to_return = finallist
    for i in range(len(head)):
        if head[i] is not None:
            finallist.next=head[i]
            while finallist.next is not None:
                finallist = finallist.next


    return to_return.next



tablica = [1.23,5.1234,2.22,8.1,3.81,7.22,0.2,9.2213,9.22,9.1,1.09,9.99]

tabins = [1.66,1.21,1.05,1.74,1.95,1.23,1.54,1.01,1.1]

#test = make_linked_list(tabins)
#test2 = select(test)
#print_Node(test2)

first1 = make_linked_list(tablica)
first2 = zadanie(first1)
print_Node(first2)