'''
Palindrome LinkedList

You have been given a head to a singly linked list of integers.
Write a function check to whether the list given is a 'Palindrome' or not.

Input format :
        The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
        Then the test cases follow.
        First and the only line of each test case or query contains the the elements of the singly linked list
        separated by a single space.
        Remember/Consider :
            While specifying the list elements for input, -1 indicates the end of the singly linked list
            and hence, would never be a list element.
Output format :
        For each test case, the only line of output that print 'true' if the list is Palindrome or 'false' otherwise.
Constraints :       1 <= t <= 10^2      0 <= M <= 10^5
Time Limit: 1sec    Where 'M' is the size of the singly linked list.

Sample Input 1 :    1                               Sample Output 1 :   true
                    9 2 3 3 2 9 -1

Sample Input 2 :    2                               Sample Output 2 :   false
                    0 2 3 2 5 -1                                        true
                    -1

Explanation for the Sample Input 2 :
For the first query, it is pretty intuitive that the the given list is not a palindrome, hence the output is 'false'.
For the second query, the list is empty. An empty list is always a palindrome , hence the output is 'true'.
'''


# METHOD 1 (By REVERSING the list)
# This method takes O(n) time and O(1) extra space.
#   1) Get the middle of the linked list.
#   2) Reverse the second half of the linked list.
#   3) Check if the first half and second half are identical.
#   4) Construct the original linked list by reversing the second half again and attaching it back to the first half
# When number of nodes are even, the first and second half contain exactly half nodes.
# The challenging thing in this method is to handle the case when number of nodes are odd.
# We don’t want the middle node as part of any of the lists as we are going to compare them for equality.
# For odd case, we use a separate variable ‘midnode’.


# Method to find Middle of LL:
# Traverse linked list using two pointers. Move one pointer by one and the other pointers by two.
# When the fast pointer reaches the end slow pointer will reach the middle of the linked list.




from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)

class Node:                     # Following is the Node class already written for the Linked List
    def __init__(self, data):
        self.data = data
        self.next = None




def isPalindrome(head):

    slow_ptr = head
    fast_ptr = head
    prev_of_slow_ptr = head                            # previous of the slow_ptr for LL with odd elements

    midnode = None                                     # To handle odd size list
    res = True                                         # Initialize result

    if (head != None and head.next != None):

        # Get the middle of the list. Move slow_ptr by 1 and fast_ptrr by 2, slow_ptr will have the middle node
        while (fast_ptr != None and fast_ptr.next != None): # Iterate till fast's next is null (fast reaches end)

            fast_ptr = fast_ptr.next.next               # increase fast by two
            prev_of_slow_ptr = slow_ptr
            slow_ptr = slow_ptr.next                    # increase slow by one

    # fast_ptr would become NULL when there are even elements in the list and not NULL for odd elements.
    # We need to skip the middle node for odd case and store it somewhere so that we can restore the original list
        if (fast_ptr != None):
            midnode = slow_ptr
            slow_ptr = slow_ptr.next

        second_half = slow_ptr                          # Now reverse the second half and compare it with first half

        prev_of_slow_ptr.next = None                    # NULL terminate first half

        second_half = reverse(second_half)              # Reverse the second half

        res = compareLists(head, second_half)           # Compare

        second_half = reverse(second_half)         # Construct the original list back. Reverse the 2nd half again

        if (midnode != None):

            # If there was a mid node (odd size case) which was not part of either first half or second half.
            prev_of_slow_ptr.next = midnode
            midnode.next = second_half
        else:
            prev_of_slow_ptr.next = second_half
    return res

# Function to reverse the linked list Note that this function may change the head
def reverse(second_half):

    prev = None
    current = second_half
    next = None
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    second_half = prev
    return second_half

def compareLists(head1, head2): # Function to check if two input lists have same data

    temp1 = head1
    temp2 = head2

    while (temp1 and temp2):
        if (temp1.data == temp2.data):
            temp1 = temp1.next
            temp2 = temp2.next
        else:
            return 0

    if (temp1 == None and temp2 == None):                   # Both are empty return 1
        return 1

    return 0                        # Will reach here when one is NULL and other is not













# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    print("\nEnter the Nodes: ")
    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()

    if isPalindrome(head):
        print('true')
    else:
        print('false')

    t -= 1