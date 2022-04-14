'''
Array Equilibrium Index

For a given array/list(ARR) of size 'N,' find and return the 'Equilibrium Index' of the array/list.
Equilibrium Index of an array/list is an index 'i' such that the sum of elements at indices [0 to (i - 1)] is
equal to the sum of elements at indices [(i + 1) to (N-1)].
One thing to note here is, the item at the index 'i' is not included in either part.
If more than one equilibrium indices are present, then
the index appearing first in left to right fashion should be returned.
Negative one(-1) if no such index is present.

Example:
Let's consider an array/list Arr = [2, 3, 10, -10, 4, 2, 9]  of size, N = 7.

There exist two equilibrium indices, one at 2 and another at 3.

At index 2, the sum of all the elements to the left, [2 + 3] is 5,
and the elements to its right, [-10 + 4 + 2 + 9] is also 5.
Hence index 2 is an equilibrium index according to the condition we want to achieve.
Mind it that we haven't included the item at index 2, which is 10, to either of the parts.

Similarly, we can see at index 3, the elements to its left sum up to 15 and to the right, sum up to 15 either.

Since index 2 comes early in the order, left to right, the answer would be 2.

Input Format :
    The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
    Then the test cases follow.
    The first line of each test case or query contains an integer 'N' representing the size of the first array/list.
    The second line contains 'N' single space separated integers representing the elements of the array/list

Output Format :
    For each test case, print the 'Equilibrium Index'.

Output for every test case will be printed in a separate line.
Constraints :       1 <= t <= 10^2      0 <= N <= 10^6

Time Limit:         1 sec
Sample Input 1 :    1                   Sample Output 1 :   2
                    5
                    1 4 9 3 2

Sample Input 2 :    2                   Sample Output 2 :   -1
                    3                                        2
                    1 4 6
                    3
                    1 -1 4
'''

from sys import stdin



# Method 1 (Simple but inefficient) (Takes more time)
# Use two loops.
# Outer loop iterates through all the element and inner loop finds out whether the current index picked
# by the outer loop is equilibrium index or not. Time complexity of this solution is O(n^2).
#
# def arrayEquilibriumIndex(arr, n):
#     for i in range(0, n):           # traverse through complete array
#         leftSum = 0
#         rightSum= 0
#         for j in range(0, i):       # get left sum
#             leftSum += arr[j]
#         for j in range(i+1, n):     # get right sum
#             rightSum += arr[j]
#         if leftSum == rightSum:     # if leftsum and rightsum are same, then we are done
#             return i
#     return -1



# Method 2 (Tricky and Efficient)
# The idea is to get the total sum of the array first.
# Then Iterate through the array and keep updating the left sum which is initialized as zero.
# In the loop, we can get the right sum by subtracting the elements one by one.
#
# 1) Initialize leftsum  as 0
# 2) Get the total sum of the array as sum
# 3) Iterate through the array and for each index i, do following.
#     a)  Update sum to get the right sum.
#            sum = sum - arr[i]
#        // sum is now right sum
#     b) If leftsum is equal to sum, then return current index.
#        // update leftsum for next iteration.
#     c) leftsum = leftsum + arr[i]
# 4) return -1
# // If we come out of loop without returning then
# // there is no equilibrium index
def arrayEquilibriumIndex(arr, n):

    leftSum = 0                             # start from left end
    total_sum = sum(arr)                    # get the total sum of array

    for i in range(0, n):                   # traverse through complete array
        # Update total sum to get the current total sum, by subtracting elements from left
        total_sum = total_sum - arr[i]

        if total_sum == leftSum:            # if left sum = sum return current index
            return i
        else:
            leftSum = leftSum + arr[i]      # if not, update left sum by adding ith element

    return -1                               # means no equilibrium index found
    # pass


# Your code goes here


# Taking input using fast I/O method
def takeInput():
    print("\nEnter the Size of Array: ")
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    print("\nEnter the Elements: ")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    print("\nEqilibrium Index of Array is: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
print("Enter the Number of Test Cases you want to perform:")
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()
    print(arrayEquilibriumIndex(arr, n))

    t -= 1