def insertionSort(alist):
    for index in range(1, len(alist), 1):
        element = alist[index]
        j = index - 1
        while(j >= 0 and alist[j] > element):
            alist[j + 1] = alist[j]
            j=j-1
        alist[j + 1] = element
    return alist

alist = [9, 8, 99, 110, 8, 87, 637, 8, 3, 13, 87, 12, 99]
newlist = insertionSort(alist)

for index in range(0, len(newlist), 1):
    print(newlist[index])
