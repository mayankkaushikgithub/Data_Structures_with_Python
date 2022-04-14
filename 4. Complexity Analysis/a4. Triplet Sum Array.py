'''
Triplet sum

You have been given a random integer array/list(ARR) and a number X.
Find and return the triplet(s) in the array/list which sum to X.

Note :  Given array/list can contain duplicate elements.

Input format :
        The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
         Then the test cases follow.
        First line of each test case or query contains an integer 'N' representing the size of the first array/list.
        Second line contains 'N' single space separated integers representing the elements in the array/list.
        Third line contains an integer 'X'.
Output format :
        For each test case, print the total number of triplets present in the array/list.
        Output for every test case will be printed in a separate line.

Constraints :       1 <= t <= 10^2      0 <= N <= 10^3      0 <= X <= 10^9
Time Limit: 1 sec

Sample Input 1:     1                                   Sample Output 1:    5
                    7
                    1 2 3 4 5 6 7
                    12

Sample Input 2:     2                                   Sample Output 2:    0
                    7                                                       5
                    1 2 3 4 5 6 7
                    19
                    9
                    2 -5 8 -6 0 5 10 11 -3
                    10
Explanation for Input 2:
Since there doesn't exist any triplet with sum equal to 19 for the first query, we print 0.
For the second query, we have 5 triplets in total that sum up to 10.
They are, (2, 8, 0), (2, 11, -3), (-5, 5, 10), (8, 5, -3) and (-6, 5, 11)

'''

from sys import stdin

# METHOD - 1        (NOT SO GOOD)
# Algorithm:
# 1. Given an array of length n and a sum s
# 2. Create three nested loop first loop runs from start to end (loop counter i),
#    second loop runs from i+1 to end (loop counter j) and third loop runs from j+1 to end (loop counter k)
# 3. The counter of these loops represent the index of 3 elements of the triplets.
# 4. Find the sum of ith, jth and kth element. If the sum is equal to given sum. Print the triplet and break.
# 5. If there is no triplet, then print that no triplet exist.
# Time Complexity: O(n3). There are three nested loops traversing the array, so the time complexity is O(n^3)
# Space Complexity: O(1). As no extra space is required.
# solution:
# def tripletSum(arr, n, num):
#     l = 0
#     count = 0
#     for i in range(l, n-2):
#         for j in range(i+1, n-1):
#             for k in range(j+1, n):
#                 if ((arr[i]+arr[j]+arr[k]) == num):
#                     count = count + 1
#                     print("Pairs: ",arr[i], arr[j], arr[k])
#                     continue
#     return count



# METHOD - 2 (using sorting & 2-pointer technique to increase efficacy)
# Algorithm :
# 1. Sort the given array.
# 2. Loop over the array and fix the first element of the possible triplet, arr[i].
# 3. Then fix two pointers, one at i + 1 and the other at n – 1. And look at the sum,
#    1. If the sum is smaller than the required sum, increment the first pointer.
#    2. Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
#    3. Else, if the sum of elements at two-pointer is equal to given sum then print the triplet and break.

def tripletSum(arr, n, num):
    arr.sort()              # Sort the elements

    if n != 0:
        for i in range(0, n - 2):           # Now fix the first element one by one and find the other two elements

    # To find the other two elements, start two index variables from two corners of the array
    # and move them toward each other

            l = i + 1                   # index of the first element in the remaining elements
            r = n - 1                   # index of the last element
            # count = 0

            while (l < r):
                count = 0

                if (arr[i] + arr[l] + arr[r] == num):
                    print("Triplet is: ", arr[i], ', ', arr[l], ', ', arr[r])
                    count = count + 1
                    l += 1
                    r -= 1
                elif (arr[i] + arr[l] + arr[r] < num):
                    l += 1
                else:  # arr[i] + arr[l] + arr[r] > num
                    r -= 1
                continue

            return count                    # If we reach here, then no triplet was found

    else:
        return 0









# taking input using fast I/O method
def takeInput():
    print("\nEnter the Size of Array: ")
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    print("\nEnter the Elements: ")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()


# main
print("Enter Number of Test Cases you want to perform: ")
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()

    print("\nEnter the Number for which you want to count pairs: ")
    num = int(stdin.readline().strip())

    print(tripletSum(arr, n, num))

    t -= 1