'''
Last Index Of Number Question

Given an array of length N & an integer x, you need to find and return the last index of integer x present in the array.
Return -1 if it is not present in the array.

Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0.

Input Format :
            Line 1 : An Integer N i.e. size of array
            Line 2 : N integers which are elements of the array, separated by spaces
            Line 3 : Integer x
Output Format :
            last index or -1
Constraints :   1 <= N <= 10^3

Sample Input :  4                   Sample Output : 3
                9 8 10 8
                8
'''

# def lastIndex(arr, x):                     # Using Recursion - 1
#     l = len(arr)
#     if l == 0:                              # base case (if no element is present in list)
#         return -1
#
#     # we want last index, so at first don't check element at first index check for remaining list & go to last
#     smallerList = arr[1:]
#     smallerListOutput = lastIndex(smallerList, x)
#     if smallerListOutput != -1:
#         return smallerListOutput +1   # +1 coz it's smaller list we need index as per original list
#     else:           # if the remaining list doesn't have the no. (smallListOutput is -1) then check for first element
#         if arr[0] == x:
#             return 0
#         else:
#             return -1



def lastIndex(arr, x, si=0):                     # Using Recursion - 2 (Better)
    l = len(arr)
    if si == l:                       # Base Case  # if 'si' (start index) is equal to 'l' means we're at end of array
        return -1

    # check for 0th element later, also no need to make new list
    smallerListOutput = lastIndex(arr, x, si+1)

    if smallerListOutput != -1:     # means it found something
        return smallerListOutput    # no need to add +1 as it is actual index
    else:                           # means no x is found in remaining list
        if arr[si] == x:            # so check in beginning element if found return its index
            return si
        else:
            return -1





# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

print("Enter the Size of Array:")
n=int(input())

print("\nEnter the Elements of Array")
arr=list(int(i) for i in input().strip().split(' '))

print("\nEnter the Element you want to search for:")
x=int(input())

print(lastIndex(arr, x))         # for method - 1
# print(lastIndex(arr, x, si=0))      # for method - 2

