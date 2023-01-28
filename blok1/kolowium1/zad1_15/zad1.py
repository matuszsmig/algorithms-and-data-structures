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
    tab = [[Node(None)] for _ in range(10)]
    tabNode = [tab[i] for i in range(10)]
    while g.next is not None:
        temp = g.next
        tabNode[9-int(temp.val)][0].next = temp
        tabNode[9 - int(temp.val)][0] = tabNode[9-int(temp.val)][0].next
        g=g.next
    for i in range(len(tab)):
        print_Node(tab[i][0])
        print()



tablica = [1.23,5.1234,2.22,8.1,3.81,7.22,0.2,9.2213,9.22,9.1,1.09]

tabins = [1.66,1.21,1.05,1.74,1.95,1.23,1.54,1.01]

#test = make_linked_list(tabins)
#test2 = select(test)
#print_Node(test2)

first1 = make_linked_list(tablica)
first2 = zadanie(first1)
print_Node(first2)