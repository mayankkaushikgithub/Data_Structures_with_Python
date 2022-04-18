'''
Bubble Sort (Iterative) LinkedList

Given a singly linked list of integers, sort it using 'Bubble Sort.'

Note :  No need to print the list, it has already been taken care. Only return the new head to the list.

Input format :
            The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
            Then the test cases follow.
            The first and the only line of each test case or query contains the elements of the singly linked list
            separated by a single space.
            Remember/Consider :
            While specifying the list elements for input, -1 indicates the end of the singly linked list
            and hence, would never be a list element
Output format :
            For each test case/query, print the elements of the sorted singly linked list.
            Output for every test case will be printed in a separate line.
Constraints :   1 <= t <= 10^2      0 <= M <= 10^3      Where M is the size of the singly linked list.
Time Limit: 1sec

Sample Input 1 :    1                               Sample Output 1 :   3 4 5 6 7 8 9 10
                    10 9 8 7 6 5 4 3 -1

Sample Output 2 :   2                               Sample Output 2 :   -5 1 5 9 10 67 89 90
                    -1
                    10 -5 9 90 5 67 1 89 -1
'''

from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    count = 0
    curr = head
    while curr is not None:
        curr = curr.next
        count += 1
    return count


def bubbleSort(head):

    if head is None:
        return head

    len = length(head)                           # length of LL

    for i in range(0, len):                       # iteration to sort each elements

        prev = None                             # previous of current working node
        curr = head                             # on which we will work

        while curr.next is not None:    # till we reach end

            if curr.data > curr.next.data:          # use PEN & PAPER

                if prev is None:                # if we've to swap first two nodes
                    nxt = curr.next
                    curr.next = nxt.next
                    nxt.next = curr
                    prev = nxt
                    head = prev

                else:                               # if we've to swap in b/w a LL
                    nxt = curr.next
                    prev.next = nxt
                    curr.next = nxt.next
                    nxt.next = curr
                    prev = nxt

            else:
                prev = curr                         # if data is equal or in ascending order
                curr = curr.next                     # increase the ptr to current & previous Node


    return head



# Your code goes here


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


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


print("Enter Total Number of Test Cases: ")
t = int(stdin.readline().rstrip())

# main
while t > 0:
    head = takeInput()

    print("\nOriginal Linked List: ")
    printLinkedList(head)

    head = bubbleSort(head)

    print("\nSorted Linked List: ")
    printLinkedList(head)

    t -= 1