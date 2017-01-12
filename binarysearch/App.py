def binarySearch(alist, x):
    p = 0
    r = len(alist) - 1
    while(p <= r):
        q = int((p + r) / 2)
        if (alist[q] > x):
            r = q - 1
        elif (alist[q] < x):
            p = q + 1
        else:
            return q
    return -1

def recursiveBinarySearch(alist, p, r, x):
    print("[ %d...%d ]" % (p, r))
    if (p > r):
        return -1
    else:
        q = int((p + r) / 2)
        if(alist[q] is x):
            return q
        elif (alist[q] > x):
            return recursiveBinarySearch(alist, p, q - 1, x)
        else:
            return recursiveBinarySearch(alist, q + 1, r, x)


alist = [1, 2, 3, 4, 7, 9, 12, 18, 20, 24, 29, 32, 34, 35, 38, 42, 43, 48, 60, 63, 65, 66, 71, 73, 76]
print(recursiveBinarySearch(alist, 0, len(alist)-1, 48))
