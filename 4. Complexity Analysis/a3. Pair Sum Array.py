'''
Pair sum in array

You have been given an integer array/list(ARR) and a number 'num'.
Find and return the total number of pairs in the array/list which sum to 'num'.

Note:   Given array/list can contain duplicate elements.
Input format :
    The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
     Then the test cases follow.
    First line of each test case or query contains an integer 'N' representing the size of the first array/list.
    Second line contains 'N' single space separated integers representing the elements in the array/list.
    Third line contains an integer 'num'.
Output format :
    For each test case, print the total number of pairs present in the array/list.
    Output for every test case will be printed in a separate line.

Constraints :       1 <= t <= 10^2      0 <= N <= 10^4      0 <= num <= 10^9

Time Limit: 1 sec
Sample Input 1:     1                                       Sample Output 1:    7
                    9
                    1 3 6 2 5 4 3 2 4
                    7
Sample Input 2:     2                                       Sample Output 2:    0
                    9                                                           2
                    1 3 6 2 5 4 3 2 4
                    12
                    6
                    2 8 10 5 -2 5
                    10

Explanation for Input 2:
Since there doesn't exist any pair with sum equal to 12 for the first query, we print 0.
For the second query, we have 2 pairs in total that sum up to 10. They are, (2, 8) and (5, 5).
'''

from sys import stdin

# Method - 1        (Takes more time)
#  A simple solution is to traverse each element and check if there’s another number in the array
#  which can be added to it to give sum. Time Complexity: O(n^2)
# def pairSum(arr, n, num):
#     k = 0
#     for i in range(0, n):
#         for j in range(i+1, n):
#             l = arr[i] + arr[j]
#             if l == num:
#                 print(arr[i], arr[j])
#                 k = k + 1
#     return k


#  Method - 2 (My solution)
# If sum is > than the sum of pairs, shift the left pointer to increase the value of required sum
# If sum is < than the sum of pairs, shift the right pointer to decrease the value
# def pairSum(arr, n, sum):
#     arr.sort()
#     print(arr)              # sorted array
#     l = 0                   # pointer for beginning of array
#     r = n - 1               # pointer for end of array
#     count = 0
#     while l < r:
#         if (arr[l] + arr[r] < sum):
#             l += 1
#         elif (arr[l] + arr[r] > sum):
#             r -= 1
#         else: #(arr[l] + arr[r] == sum):
#             print(arr[l], arr[r])       # pairs with sum = num
#             if(arr[l] == arr[l+1]):
#                 count += 1
#                 l += 1
#             else:
#                 r -= 1
#     return count



# METHOD - 2    (Coding Ninjas Solution)
def pairSum(arr, x):
    n = len(arr)
    i = 0
    j = n - 1
    while i < j:
        if arr[i] + arr[j] > x:
            j = j - 1
        elif arr[i] + arr[j] < x:
            i = i + 1
        else:
            product = 0
            if arr[i] == arr[j]:
                count = j - i + 1
                i = j
                product = count * (count - 1) // 2
            else:
                count1 = 1
                count2 = 1
                while arr[i] == arr[i + 1] and i + 1 < j:
                    count1 += 1
                    i += 1
                while arr[j] == arr[j - 1] and j - 1 > i:
                    count2 += 1
                    j -= 1
                product = count1 * count2

            for a in range(0, product):
                print(arr[i], arr[j])
            i += 1
            j -= 1
    return product





# taking INPUT using fast I/O method
def takeInput():
    print("\nEnter the Size of Array: ")
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0

    print("\nEnter the Elements: ")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
print("Enter Number of Test Cases you want to perform:")
t = int(stdin.readline().strip())

while t > 0:
    arr, n = takeInput()

    print("\nEnter the Number for which you want to count pairs: ")
    num = int(stdin.readline().strip())

    # print(pairSum(arr, n, num))
    print(pairSum(arr, num))

    t -= 1

