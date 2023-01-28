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

def selectionSortLadniejszy(p,k):
    g=Node(None)
    g.next = p
    toreturn = g
    while g.next:
        prev = g
        curr = prev.next
        minn = curr
        licznik = 0
        flag = False
        if prev.val==curr.val:
            g=g.next
        else:
            while licznik <= k and curr is not None:
                if minn==0 or curr.val<minn.val:
                    minn = curr
                    prevminn=prev
                    if minn.next is not None:
                        nextminn=minn.next
                        flag = True
                prev=curr
                curr=curr.next
                licznik+=1
            if flag:
                minn.next=prevminn
                prevminn.next = nextminn
                g.next = minn
            g = g.next
            #print(g.val,g.next.val,g.next.next.val)

    return toreturn.next

def selectionSort(p,k):
    g=Node(None)
    g.next = p
    toreturn = g
    while g.next:
        curr = g.next
        prev = g
        minn = 0
        licznik = 0
        if prev.val==curr.val:
            g=g.next
        else:
            while licznik <= k and curr is not None:
                if minn==0 or curr.val<minn.val:
                    minn = curr
                    prevminn=prev
                    if minn.next is not None:
                        nextminn=minn.next
                prev=curr
                curr=curr.next
                licznik+=1
            if k == 1:
                if prevminn.val is not None and prevminn.val > minn.val:
                    minn.next = prevminn
                prevminn.next = nextminn
                g.next = minn
                g = g.next
            else:
                if minn.next is None:
                    if prevminn.val == g.next.val:
                        g.next = minn
                        g.next.next = prevminn
                        prevminn.next = None
                    else:
                        tmp=g.next.next
                        temp = g.next
                        g.next = minn
                        g.next.next = tmp
                        prevminn.next = temp
                        prevminn.next.next=None
                elif prevminn.val == g.next.val:
                    g.next = minn
                    g.next.next = prevminn
                    prevminn.next = nextminn
                else:
                    tmp = g.next
                    temp = g.next.next
                    g.next = minn
                    g.next.next
                    g.next.next = temp
                    prevminn.next= tmp
                    prevminn.next.next=nextminn
                g = g.next

    return toreturn.next



tab = [2, 6, 6,6,6,6,6, 10, 29, 24, 31, 43, 36, 45, 51, 49, 52, 56, 53, 56, 61, 58, 71, 75, 72, 79, 93, 82, 99]
first1 = make_linked_list(tab)
first2 = selectionSort(first1,1)
print_Node(first2)