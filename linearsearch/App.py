def linearSearch(alist, x):
    for index in range(0, len(alist), 1):
        if alist[index] is x:
            return index
    return -1

def recursiveLinearSearch(alist, i, x):
    if (i > len(alist) - 1):
        return -1
    elif (alist[i] is x):
        return i
    else:
        print("index at: %d" % i)
        return recursiveLinearSearch(alist, i + 1, x)


alist = [54, 67, 21, 3, 12, 1, 76, 39, 11]
print(recursiveLinearSearch(alist, 0, 39))
