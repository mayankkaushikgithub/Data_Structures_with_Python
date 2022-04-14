'''
Check Number in Array

Given an array of length N and an integer x, you need to find if x is present in the array or not. Return true or false.
Do this recursively.

Input Format :
                    Line 1 : An Integer N i.e. size of array
                    Line 2 : N integers which are elements of the array, separated by spaces
                    Line 3 : Integer x
Output Format :     'true' or 'false'
Constraints :       1 <= N <= 10^3

Sample Input 1 :    3                       Sample Output 1 :   true
                    9 8 10
                    8
Sample Input 2 :    3                       Sample Output 2 :   false
                    9 8 10
                    2
'''

# def checkNumber(arr, x):              # without using recursion
#     for i in range(len(arr)):
#         if arr[i] == x:
#             return True

def checkNumber(arr, x):                # using recursion

    if len(arr) == 0:
        return False

    if arr[0] == x:
        return True

    else:
        return checkNumber(arr[1:], x)
    # pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

print("Enter the Size of Array:")
n=int(input())

print("\nEnter the Elements of Array:")
arr=list(int(i) for i in input().strip().split(' '))

print("\nEnter the Number you want to search for:")
x=int(input())

if checkNumber(arr, x):
    print('true')
else:
    print('false')



