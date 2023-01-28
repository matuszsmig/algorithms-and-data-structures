def heapify(tab, n, i):
    max_ind = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and tab[max_ind] < tab[left]:
        max_ind = left
    if right < n and tab[max_ind] < tab[right]:
        max_ind = right
    if max_ind != i:
        tab[i], tab[max_ind] = tab[max_ind], tab[i]
        heapify(tab, n, max_ind)


def build_heap(tab):
    n = len(tab)
    for i in range(n//2-1, -1, -1):
        heapify(tab,n,i)

def heapsort(tab):
    n = len(tab)
    build_heap(tab)
    for i in range(n-1,0,-1):
        tab[0],tab[i]=tab[i],tab[0]
        heapify(tab,i,0)
    return tab



tab = [5,4,8,9,3,2,6,1,7]
print(heapsort(tab))