
def selectionSort(alist):
    for index in range(0,len(alist),1):
        minimum = index
        for index2 in range(index + 1, len(alist), 1):
            if (alist[index2] < alist[minimum]):
                minimum = index2
        temp = alist[index]
        alist[index] = alist[minimum]
        alist[minimum] = temp

alist = [54, 67, 21, 3, 12, 1, 76, 39, 11]
selectionSort(alist)
print(alist)
