'''
Delete every N nodes

You have been given a singly linked list of integers along with two integers, 'M,' and 'N.'
Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes.
Continue the same until the end of the linked list.
To put it in other words, in the given linked list, you need to delete N nodes after every M nodes.

Note :  No need to print the list, it has already been taken care. Only return the new head to the list.

Input format :
        The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
            Then the test cases follow.
        The first line of each test case or query contains the elements of the singly linked list
            separated by a single space.
        The second line of input contains two integer values 'M,' and 'N,' respectively.
        A single space will separate them.
        Remember/Consider :
        While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element
Output format :
        For each test case/query, print the elements of the updated singly linked list.
        Output for every test case will be printed in a seperate line.

Constraints :       1 <= t <= 10^2      0 <= P <= 10^5      Where P is the size of the singly linked list.
                    0 <= M <= 10^5      0 <= N <= 10^5
Time Limit: 1sec

Sample Input 1 :    1                                       Sample Output 1 :   1 2 5 6
                    1 2 3 4 5 6 7 8 -1
                    2 2
Sample Input 2 :    2                                       Sample Output 2 :   1 2 6 7
                    10 20 30 40 50 60 -1
                    0 1
                    1 2 3 4 5 6 7 8 -1
                    2 3
Explanation of Sample Input 2 :
For the first query, we delete one node after every zero elements hence removing all the items of the list.
Therefore, nothing got printed.
For the second query, we delete three nodes after every two nodes, resulting in the final list,
1 -> 2 -> 6 -> 7.
'''

from sys import stdin


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def skipMdeleteN(head, M, N):

# M = 0 means we delete one node after every zero elements hence removing all the items of the list.
    if M == 0:                              # so we don't return anything
        return None

    temp1 = head                          # make a pointer to head
    while temp1 is not None:              # main loop that traverse through whole LL

        count1 = 1
        while count1 < M:                   # skip M nodes
            if temp1 is None:               # if nothing is in the LL return head
                return head
            else:
                temp1 = temp1.next          # move ptr to next node till we skip M elements
                count1 += 1

        if temp1 is None:
            return head


        count2 = 1                          # this one is for node to be skipped
        temp2 = temp1.next                  # join temp2 with last Mth node
        while count2 <= N:                  # run till all the ptr is at last of nodes to be skipped
            if temp2 is None:               # this means no node is present after Mth node
                break                       # so break
            else:
                temp2 = temp2.next
                count2 += 1

        temp1.next = temp2                  # join the last temp1 with temp2, as we've skipped N nodes
        temp1 = temp2                       # set current ptr for next iteration

    return head

    # pass


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


def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()
    m_n = stdin.readline().strip().split(" ")

    m = int(m_n[0])
    n = int(m_n[1])

    newHead = skipMdeleteN(head, m, n)
    printLinkedList(newHead)

    t -= 1