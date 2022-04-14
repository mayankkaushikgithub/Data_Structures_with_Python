'''
First Index of Number - Question

Given an array of length N and an integer x, you need to find and return the first index of integer x present in the array. Return -1 if it is not present in the array.
First index means, the index of first occurrence of x in the input array.
Do this recursively. Indexing in the array starts from 0.

Input Format :
                Line 1 : An Integer N i.e. size of array
                Line 2 : N integers which are elements of the array, separated by spaces
                Line 3 : Integer x
Output Format :
                first index or -1
Constraints :   1 <= N <= 10^3

Sample Input :  4                  Sample Output : 1
                9 8 10 8
                8
'''


# def checkNumber(arr, x):                # NOT using recursion
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return i



# def firstIndex(arr, x):                     # Using Recursion - 1
#     l = len(arr)
#     if l == 0:
#         return -1
#     if arr[0] == x:
#         return 0
#     smallerList = arr[1:]
#     smallerListOutput = firstIndex(smallerList, x)
#     if smallerListOutput == -1:
#         return -1
#     else:
#         return 1+smallerListOutput

def firstIndex(arr, x, si=0):                     # Using Recursion - 2
    l = len(arr)

    if si == l:             # Base Case  # if 'si' (start index) is equal to 'l' means we're at end of array
        return -1

    if arr[si] == x:        # this means: if index of number is found, return the index
        return si

    smallerListOutput = firstIndex(arr, x, si+1) # else call the function again with next starting index i.e.+1
    return smallerListOutput
    # pass



# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

print("Enter the Size of Array:")
n=int(input())

print("\nEnter the Elements of Array")
arr=list(int(i) for i in input().strip().split(' '))

print("\nEnter the Element you want to search for:")
x=int(input())

# print(firstIndex(arr, x))         # for method - 1
print(firstIndex(arr, x, si=0))      # for method - 2

