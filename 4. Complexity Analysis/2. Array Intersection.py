'''
Array Intersection

You have been given two integer arrays/list(ARR1 and ARR2) of size N and M, respectively.
You need to print their intersection; An intersection for this problem can be defined
when both the arrays/lists contain a particular value or to put it in other words,
when there is a common value that exists in both the arrays/lists.

Note :  Input arrays/lists can contain duplicate elements.

The intersection elements printed would be in the order they appear in the first sorted array/list(ARR1).

Input format :
    The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
    Then the test cases follow.
    The first line of each test case or query contains an integer 'N' representing the size of the first array/list.
    The second line contains 'N' single space separated integers representing the elements of the first the array/list.
    The third line contains an integer 'M' representing the size of the second array/list.
    The fourth line contains 'M' single space separated integers representing the elements of the second array/list.
Output format :
    For each test case, print the intersection elements in a row, separated by a single space.
    Output for every test case will be printed in a separate line.

Constraints :       1 <= t <= 10^2      0 <= N <= 10^6      0 <= M <= 10^6
Time Limit: 1 sec

Sample Input 1 :        2                               Sample Output 1 :       2 3 4
                        6                                                       10
                        2 6 8 5 4 3
                        4
                        2 3 4 7
                        2
                        10 10
                        1
                        10

Sample Input 2 :        1                               Sample Output 2 :       1 2 2
                        4
                        2 6 1 2
                        5
                        1 2 3 4 2

Explanation for Sample Output 2 :
Since, both input arrays have two '2's, the intersection of the arrays also have two '2's.
The first '2' of first array matches with the first '2' of the second array.
Similarly, the second '2' of the first array matches with the second '2' if the second array.
'''

from sys import stdin


def intersection(arr1, arr2, n, m):         # Soln. 1
    i = 0
    j = 0
    arr1.sort()
    # print(arr1)   # arr1 after sorting
    arr2.sort()
    # print(arr2)   # arr2 after sorting

    while (i < n and j < m):
        if (arr1[i] > arr2[j]):
            j += 1
        # else:
        elif (arr2[j] > arr1[i]):
            i += 1
        else:
            # when both are equal
            print(arr1[i], end=" ")
            i += 1
            j += 1

# def intersection(arr1, arr2, n, m):           # Soln. 2
    # arr3 = []
    # for i in range(len(arr1)):
    #     for j in range(len(arr2)):
    #         if arr1[i] == arr2[j]:
    #             arr3.append(arr1[i])
    #             arr2[j] = -1
    #             # break
    # print(arr3)




# Taking input using fast I/O method
def takeInput():
    print("\nEnter the Size of Array:")
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), 0

    print("\nEnter the Elements of Array:")
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


# main
print("Enter the Number of Test Cases you want to perform:")
t = int(stdin.readline().strip())

while t > 0:
    arr1, n = takeInput()
    arr2, m = takeInput()
    intersection(arr1, arr2, n, m)
    print()

    t -= 1