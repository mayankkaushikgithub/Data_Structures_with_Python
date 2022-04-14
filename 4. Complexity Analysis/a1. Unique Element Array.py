'''
Find the Unique Element

You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
You need to find and return that number which is unique in the array/list.

Note:   Unique element is always present in the array/list according to the given condition.

Input format :
    The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
    Then the test cases follow.
    First line of each test case or query contains an integer 'N' representing the size of the array/list.
    Second line contains 'N' single space separated integers representing the elements in the array/list.

Output Format :
    For each test case, print the unique element present in the array.

Output for every test case will be printed in a separate line.
Constraints :       1 <= t <= 10^2      0 <= N <= 10^6
Time Limit: 1 sec

Sample Input 1:     1                           Sample Output 1:    1
                    7
                    2 3 1 6 3 6 2

Sample Input 2:     2                           Sample Output 2:    4
                    5                                               10
                    2 4 7 2 7
                    9
                    1 3 1 3 6 6 7 10 7
'''

from sys import stdin


# def findUnique(arr, n):                           #Soln. 1 (Too Slow)
#     for i in range(0, n):
#         for j in range(0, n):
#             if (i!=j) and (arr[i]==arr[j]):
#                 break
#             else:
#                 j = j + 1
#         if j == n:
#             return arr[i]


# Soln. 2   The best solution is to use XOR.
            # XOR of all array elements gives us the number with a single occurrence.
            # The idea is based on the following two facts.
            # a) XOR of a number with itself is 0.
            # b) XOR of a number with 0 is number itself.
def findUnique(arr, n):
    res = arr[0]
    for i in range(1, n):
        res = res ^ arr[i]
    return res





# Your code goes here


# taking input using fast I/O method
def takeInput():
    print("\nEnter the Size: ")
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    print("\nEnter the Elements: ")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    print("\nUnique Element: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
print("Enter the Number of Test Cases you want to perform: ")
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1