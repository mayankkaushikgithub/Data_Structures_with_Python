'''
Even after Odd LinkedList

For a given singly linked list of integers, arrange the elements such that
all the even numbers are placed after the odd numbers.
The relative order of the odd and even terms should remain unchanged.

Note :  No need to print the list, it has already been taken care. Only return the new head to the list.

Input format:
        The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
            Then the test cases follow.
        The first line of each test case or query contains the elements of the singly linked list
        separated by a single space.
        Remember/Consider :
        While specifying the list elements for input, -1 indicates the end of the singly linked list
        and hence, would never be a list element
Output format:
        For each test case/query, print the elements of the updated singly linked list.
        Output for every test case will be printed in a seperate line.
Constraints :       1 <= t <= 10^2      0 <= M <= 10^5      Where M is the size of the singly linked list.
Time Limit: 1sec

Sample Input 1 :    1                           Sample Output 1 :   1 5 4 2
                    1 4 5 2 -1
Sample Input 2 :    2                           Sample Output 2 :   1 11 3 9 6 8 0
                    1 11 3 6 8 0 9 -1                               10 20 30 40
                    10 20 30 40 -1
'''

from sys import stdin

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def evenAfterOdd(head):

    oh = None       # for Odd LL
    ot = None
    eh = None       # for Even LL
    et = None

    if head is None:        # if nothing is present in LL
        return head

    while head is not None:

        if head.data % 2 != 0:
            if oh is None:
                oh = head
                ot = head
                # head = head.next
            else:
                ot.next = head
                ot = ot.next
                # head = head.next

        elif head.data % 2 == 0:
            if eh is None:
                eh = head
                et = head
                # head = head.next
            else:
                et.next = head
                et = et.next
                # head = head.next
        head = head.next

    if oh is None:                  # if whole LL contains Even Value Nodes
        et.next = None              # break the LL by adding None to last
        return eh                   # return head of Even LL

    elif eh is None:                # if whole LL contains Odd Value Nodes
        ot.next = None              # break the LL by adding None to last of ODD LL
        return oh                   # return head of Odd LL

    else:                           # if LL contains mix of both Even & Odd Values
        et.next = None              # break the even LL
        ot.next = None              # break the Odd LL
        ot.next = eh                # connecting tail of Odd LL with head of Even LL

        return oh                   # return head of Odd LL



# Your code goes here


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

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
    newHead = evenAfterOdd(head)
    printLinkedList(newHead)

    t -= 1