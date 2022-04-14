# MERGE SORT

'''
Merge Sort Code

Sort an array A using Merge Sort.
Change in the input array itself. So no need to return or print anything.

Input format :      Line 1 : Integer n i.e. Array size
                    Line 2 : Array elements (separated by space)
Output format :     Array elements in increasing order (separated by space)
Constraints :       1 <= n <= 10^3

Sample Input 1 :    6                           Sample Output 1 :   2 3 4 5 6 8
                    2 6 8 5 4 3
Sample Input 2 :    5                           Sample Output 2 :   1 2 2 3 5
                    2 1 5 2 3
'''

# TIME COMPLEXITY
# Merge sort always divides the array in two halves and takes linear time to merge two halves.
# As we have already learned in Binary Search that whenever we divide a number into half in every step,
# it can be represented using a logarithmic function, which is log n and the number of steps
# can be represented by log n + 1(at most)
#
# And to merge the subarrays, made by dividing the original array of n elements, a running time of O(n) will be required.
#
# Hence the total time for mergeSort function will become n(log n + 1), which gives us a time complexity of O(n*log n).

def merge(L, R, a):
    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            a[k] = L[i]
            k += 1
            i += 1
        else:
            a[k] = R[j]
            k += 1
            j += 1

    while i < len(L):
        a[k] = L[i]
        k += 1
        i += 1
    while j < len(R):
        a[k] = R[j]
        k += 1
        j += 1
    return

def mergeSort(a, si, ei):
    if len(a) == 0 or len(a) == 1:
        return

    mid = len(a)//2
    L = a[0:mid]
    R = a[mid:]

    mergeSort(L, 0, 0)
    mergeSort(R, 0, 0)

    return merge(L, R, a)


print("Enter Size of Array:")
n=int(input())

print("\nEnter the Elements:")
arr=list(int(i) for i in input().strip().split(' '))

mergeSort(arr, 0, n)
# mergeSort(arr)
print(*arr)



