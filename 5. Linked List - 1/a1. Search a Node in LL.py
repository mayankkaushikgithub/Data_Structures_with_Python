'''
Find a Node in Linked List

You have been given a singly linked list of integers.
Write a function that returns the index/position of an integer data denoted by 'N' (if it exists). Return -1 otherwise.
Note : Assume that the Indexing for the singly linked list always starts from 0.

Input format :
    The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
    Then the test cases follow.
    The first line of each test case or query contains the elements of the singly linked list
    separated by a single space.
    The second line contains the integer value 'N'. It denotes the data to be searched in the given singly linked list.
    Remember/Consider : While specifying the list elements for input, -1 indicates the end of the singly linked list
    and hence, would never be a list element.
Output format :
    For each test case/query, return the index/position of 'N' in the singly linked list. Return -1, otherwise.
    Output for every test case will be printed in a separate line.
Constraints :    1 <= t <= 10^2      0 <= M <= 10^5     Where 'M' is the size of the singly linked list.
Time Limit: 1 sec

Sample Input 1 :        2                                           Sample Output 1 :       2
                        3 4 5 2 6 1 9 -1                                                    -1
                        5
                        10 20 30 40 50 60 70 -1
                        6

Sample Input 2 :        1                                           Sample Output 2 :       4
                        3 4 5 2 6 1 9 -1
                        6
Explanation for Sample Input 2 :
For the given singly linked list, considering the indices starting from 0,
progressing in a left to right manner with a jump of 1, then the N = 6 appears at position 4.
'''

from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Iterative Solution
#
# 2) Initialize a node pointer, current = head.
# 3) Do following while current is not NULL
#     a) current->key is equal to the key being searched return true.
#     b) current = current->next
# 4) Return false
def findNode(head, n):
    current = head
    count = 0
    while current is not None:
        if current.data == n:       # check if data in current node is equal to n
            return count
        count += 1
        current = current.next
    return False





# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    print("\nEnter values of Nodes: ")
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
print("Enter Total Test Cases: ")
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()

    print("\nEnter Index of data to be searched: ")
    n = int(stdin.readline().rstrip())
    print(findNode(head, n))

    t -= 1