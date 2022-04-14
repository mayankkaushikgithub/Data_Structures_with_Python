'''
Duplicate in array

You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2).
Each number is present at least once.
That is, if N = 5, the array/list constitutes values ranging from 0 to 3, and among these,
there is a single integer value that is present twice.
You need to find and return that duplicate number present in the array.

Note :  Duplicate number is always present in the given array/list.

Input format :
    The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
    Then the test cases follow.
    First line of each test case or query contains an integer 'N' representing the size of the array/list.
    Second line contains 'N' single space separated integers representing the elements in the array/list.
Output Format :
    For each test case, print the duplicate element in the array/list.

Output for every test case will be printed in a separate line.
Constraints :       1 <= t <= 10^2      0 <= N <= 10^6

Time Limit: 1 sec
Sample Input 1:     1                               Sample Output 1:    7
                    9
                    0 7 2 5 4 7 1 3 6
Sample Input 2:     2                               Sample Output 2:    1
                    5                                                   3
                    0 2 1 3 1
                    7
                    0 3 1 5 4 3 2
'''

from sys import stdin



# Method 1 (Basic)
# Use two loops.
# In the outer loop, pick elements one by one & count the number of occurrences of the picked element in the inner loop.
# def findDuplicate(arr, n):
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] == arr[j]:
#                 return arr[i]
#     return -1

# Method 2
def findDuplicate(arr, n):
    res = sum(arr)
    Sum = 0

    n_sum = ((n-2)*(n-1))//2
    # for i in range(0, n-2):
    #     Sum = Sum + arr[i]

    return res - n_sum



# Your code goes here


# Taking input using fast I/O method
def takeInput():
    print("\nEnter the Size of Array: ")
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    print("\nEnter the Elements: ")
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


# main
print("Enter the Number of Test Cases you want to perform: ")
t = int(stdin.readline().rstrip())

while t > 0:
    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1