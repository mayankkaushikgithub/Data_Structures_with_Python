'''
Delete node

You have been given a linked list of integers.
Your task is to write a function that deletes a node from a given position, 'pos'.

Note :  Assume that the Indexing for the linked list always starts from 0.

If the position is greater than or equal to the length of the linked list,
you should return the same linked list without any change.

Input format :
        The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
            Then the test cases follow.
        The first line of each test case or query contains the elements of the linked list separated by a single space.
        The second line of each test case contains the integer value of 'pos'.
            It denotes the position in the linked list from where the node has to be deleted.
        Remember/Consider : While specifying the list elements for input,
            -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
        For each test case/query, print the resulting linked list of integers in a row, separated by a single space.
        Output for every test case will be printed in a separate line.
        You don't need to print explicitly, it has been taken care of.

Constraints :       1 <= t <= 10^2      0 <= N <= 10^5      pos >= 0    Where 'N' is the size of the singly linked list.
Time Limit: 1sec

Sample Input 1 :    1                               Sample Output 1 :   3 4 5 6 1 9
                    3 4 5 2 6 1 9 -1
                    3
Sample Input 2 :    2                               Sample Output 2 :   4 5 2 6 1 9
                    3 4 5 2 6 1 9 -1                                    10 20 30 40 50 60
                    0
                    10 20 30 40 50 60 -1
                    7

'''

from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ITERATIVE FUNCTION
# def deleteNodeIteratively(head, pos):
#     # we can't actually delete a node but can delete its references(head, next)
#     if head == None:                # If linked list is empty bahara aajao
#         return -1
#
#     temp = head                     # Store head node in a temporary variable
#     if pos == 0:                    # Case-1. If head needs to be removed
#         head = temp.next            # make the  immediate next node as head
#         temp = None                 # remove temp as it's no longer needed
#         return head
#
#     for i in range(pos - 1):        # Case-2. Find previous node of the node to be deleted
#         temp = temp.next            # move temp to just previous position of 'pos'
#         if temp is None:
#             break
#
#     if temp is None:                # If position is more than number of nodes
#         return head
#     if temp.next is None:
#         return head
#
#     # Node temp.next is the node to be deleted store pointer to the next of node to be deleted
#     next = temp.next.next           # 'next' of 'prev node' will point to 'data' of 'next-to-next' node
#     temp.next = None                # Unlink the node from linked list
#     temp.next = next                # now 'prev-node' will point to 'next-to-next' node
#     return head



# RECURSIVE FUNCTION
# We recursively reduce value of k.
# When k reaches 1, we delete current node and return next of current node as new node.
# When function returns, we link the returned node as next of previous node.
def deleteNodeRecursively(head, pos):
    if pos < 1:                         # if invalid position is given
        return head
    if head == None:
        return None
    if pos == 1:                        # Base case (start needs to be deleted)
        res = head.next
        return res
    head.next = deleteNodeRecursively(head.next, pos-1)
    return head





# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None
    print("\nEnter the Values of Nodes: ")
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
    # print("None")
    print()


# main
print("Enter Total Number of Test Cases: ")
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()

    print("\nEnter the Position at which, Node is to be deleted: ")
    pos = int(stdin.readline().rstrip())

    # h = deleteNodeIteratively(head, pos)
    h = deleteNodeRecursively(head, pos)
    printLinkedList(h)

    t -= 1