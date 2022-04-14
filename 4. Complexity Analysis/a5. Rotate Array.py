'''
Rotate array

You have been given a random integer array/list(ARR) of size N.
Write a function that rotates the given array/list by D elements(towards the left).

Note:   Change in the input array/list itself. You don't need to return or print the elements.

Input format :
        The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
         Then the test cases follow.
        First line of each test case or query contains an integer 'N' representing the size of the array/list.
        Second line contains 'N' single space separated integers representing the elements in the array/list.
        Third line contains the value of 'D' by which the array/list needs to be rotated.
Output Format :
        For each test case, print the rotated array/list in a row separated by a single space.
        Output for every test case will be printed in a separate line.

Constraints :       1 <= t <= 10^4      0 <= N <= 10^6      0 <= D <= N
Time Limit: 1 sec

Sample Input 1:     1                               Sample Output 1:    3 4 5 6 7 1 2
                    7
                    1 2 3 4 5 6 7
                    2

Sample Input 2:     2                               Sample Output 2:    1 2 3 4 5 6 7
                    7                                                   3 4 1 2
                    1 2 3 4 5 6 7
                    0
                    4
                    1 2 3 4
                    2

'''

from sys import stdin

# # METHOD - 1
# def rotate(arr, n, d):
#     for i in range(0, d):           # run for total of 'factor by which you want to remove'
#         temp = arr[0]               # first store the 1st element in a temporary variable
#         for j in range(0, n-1):
#             arr[j] = arr[j+1]       # shift rest of the elements by 1 to left
#         arr[n-1] = temp             # insert the value(1st ele) stored in temporary var. to last position


# METHOD - 2
def reverse(arr, si, ei):               # reverse the original array as per condition
    while si < ei:
        arr[si], arr[ei] = arr[ei], arr[si]     # swapping the elements
        si += 1                                 # increase/decrease the pointer
        ei -= 1

def rotate(arr, n, d):
    reverse(arr, 0, n-1)                # reverse the whole array
    reverse(arr, n-d, n-1)              # reverse elements to be rotated
    reverse(arr, 0, n-d-1)              # reverse rest of the array


# Your code goes here


# Taking Input Using Fats I/O
def takeInput():
    print("\nEnter the Size of Array: ")
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    print("\nEnter the Elements of Array: ")
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# to print the array/list
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
print("Enter Number of Test Cases you want to perform: ")
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()

    print("\nEnter the Factor by which you want to rotate: ")
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    printList(arr, n)

    t -= 1