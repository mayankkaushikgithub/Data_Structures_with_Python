# THIS IS LENGTHY & ACQUIRES MORE SPACE
# def isListSorted(n):
#     l = len(n)
#     if l == 0 or l == 1:                # checking for base cases
#         return True
#     if n[0] > n[1]:
#         return False
#
#     smallerlist = n[1:]         # this will copy rest of the elements, starting from index 1 to n
#     is_smallerlist_sorted = isListSorted(smallerlist)
#
#     if is_smallerlist_sorted:
#         return True
#     else:
#         return False
#
# n = [1, 2, 3, 4, 5, 6]
# m = [10, 2, 13, 44, 5, 16]
#
# print(isListSorted(n))
# print(isListSorted(m))




# Better Version
def isListSorted(n, si):            # here we're providing Start Index to

    l = len(n)
    if l == si or si == l-1:
        return True
    if n[si] > n[si+1]:
        return False
    else:
        return isListSorted(n, si+1)




    if is_smallerlist_sorted:
        return True
    else:
        return False

n = [1, 2, 3, 4, 5, 6]
m = [10, 2, 13, 44, 5, 16]

print(isListSorted(n, 0))
print(isListSorted(m, 0))
