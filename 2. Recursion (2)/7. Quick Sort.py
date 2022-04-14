'''
Quick Sort Code

Sort an array A using Quick Sort.
Change in the input array itself. So no need to return or print anything.

Input format :      Line 1 : Integer n i.e. Array size
                    Line 2 : Array elements (separated by space)
Output format :     Array elements in increasing order (separated by space)
Constraints :       1 <= n <= 10^3

Sample Input 1 :    6                           Sample Output 1 :   2 3 4 5 6 8
                    2 6 8 5 4 3
Sample Input 2 :    5                           Sample Output 2 :   1 2 3 5 7
                    1 5 2 7 3
'''


def partition(a, si, ei):
    pivot = a[si]       # assign first element as pivot element
    count = 0

    for i in range(si, ei+1):   # pick the 1st element first make it reach its right position
        if a[i] < pivot:        # count how many elements are smaller than pivot
            count += 1
    # shift your element by 'count' no. of position to make space for small elements
    a[si+count], a[si] = a[si], a[si+count] # swap the pivot
    pivot_index = si + count

    i = si
    j = ei
    while i < j:
        # (a[i]<pivot) and (a[j]>=pivot) b'coz distant moved by i & j should be same
        if a[i] < pivot:            # when elements on left are smaller than pivot
            i = i + 1
        elif a[j] >= pivot:         # when elements on right are greater than pivot
            j = j - 1
        else:
    # this case is when you've element on left greater than pivot & an element on right less than pivot,
    #   so swap them
            a[i], a[j] = a[j], a[i]
            i = i + 1       # move i to right
            j = j - 1       # move j to left

    return pivot_index


def quick_Sort(arr, si, ei):

    if si >= ei:     # either si & ei crossed each other or they're equal
        return

    pivot_index = partition(arr, si, ei)

    quick_Sort(arr, si, pivot_index-1)
    quick_Sort(arr, pivot_index+1, ei)


print("Enter the Size of Array:")
n=int(input())

print("\nEnter the Elements of Array:")
arr=list(int(i) for i in input().strip().split(' '))

# l = len(arr)
quick_Sort(arr, 0, len(arr)-1)
print(*arr)
