def binarySearch(a, x, si, ei):

    if si > ei:         # Base Case
        return -1

    mid = (si+ei)//2

    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return binarySearch(a, x, si, mid-1) # si remains same
    else:
        return binarySearch(a, x, mid+1, ei)
    # pass

a = [1, 3, 5, 7, 9, 11, 13, 15, 16, 17]
l = len(a)
x = int(input())
res = binarySearch(a, x, 0, l)



