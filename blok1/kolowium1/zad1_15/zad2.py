def partition(T,left,right):
    pivot = T[right]
    i = left-1
    for j in range(left,right):
        if T[j]<pivot:
            i+=1
            T[i],T[j]=T[j],T[i]
    T[right],T[i+1]=T[i+1],T[right]
    return i+1

def quickselect(T,left,right, number):
    index = partition(T,left,right)
    if index-left==number-1:
        return T[index]
    if index-left>number-1:
        return quickselect(T,left,index-1,number)
    return quickselect(T,index+1,right,number-index+left-1)

def sumbetween(T, fromm, too):
    quickselect(T, 0, len(T)-1, fromm)
    quickselect(T, fromm, len(T) - 1, too-fromm)
    sum = 0
    for i in range(fromm,too+1):
        sum+=T[i]
    return sum

tab = [20, 11, 16, 53, 70, 91, 95, 17, 81, 69, 8, 3, 94, 98, 20, 1, 27, 73, 64, 49, 49, 67, 48, 1, 25, 70, 12, 72, 85, 44, 34, 99, 44, 63, 51, 22, 6, 17, 7, 93, 56, 93, 70, 69, 83, 91, 73, 8, 70, 57, 42, 47, 0, 91, 86, 75, 22, 39, 47, 52, 41, 81, 16, 80, 21, 55, 55, 67, 76, 20, 60, 68, 57, 3, 56, 0, 68, 97, 16, 94, 98, 53, 74, 49, 10, 44, 64, 57, 84, 64, 14, 47, 25, 34, 30, 99, 75, 58, 84, 13]
print(sumbetween(tab, 3, 10))
print(tab)

#print(quickselect(tab,0,len(tab)-1))