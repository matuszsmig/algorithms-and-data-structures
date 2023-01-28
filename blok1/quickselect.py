def partition(T,left,right):
    pivot = T[right]
    i = left - 1
    for j in range(left,right):
        if T[j]<=pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[i+1],T[right]=T[right],T[i+1]
    return i+1

def quickselect(T,left,right,number):
    index = partition(T,left,right)
    if index-left == number-1:
        return T[index]
    if index - left > number - 1:
        return quickselect(T,left,index-1,number)
    return quickselect(T, index+1, right, number-index+left-1)

tab=[2,54,1,2,5,2,3,5,32,3,6,7,12,767,42,6,3,87,2,7,4,23,5,56,1,23]
print(quickselect(tab,0,len(tab)-1,7))
print(tab)