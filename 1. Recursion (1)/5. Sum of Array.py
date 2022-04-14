'''
Sum Of Array

Given an array of length N, you need to find and return the sum of all elements of the array.
Do this recursively.

Input Format :      Line 1 : An Integer N i.e. size of array
                    Line 2 : N integers which are elements of the array, separated by spaces
Output Format :     Sum
Constraints :       1 <= N <= 10^3

Sample Input 1 :    3               Sample Output 1 :   26
                    9 8 9
Sample Input 2 :    3               Sample Output 2 :   7
                    4 2 1
'''



# def sumArray(arr):                # without using recursion
#     sum = 0
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#     return sum


def sumArray(arr):                  # using recursion

    l = len(arr)

    if l == 0:                      # checking Base Case 1
        return 0

    if l == 1:                      # checking Base Case 2
        return arr[0]

    else:
        a = sumArray(arr[1:])       # take the hypothesis to be true for f(k)
        return arr[0] + a           # prove it to be true for f(k+1)

    # Please add your code here



# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

print("Enter the Size of Array:")
n=int(input())

print("\nEnter the Elements of Array:")
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr))
