'''
Length of LL

For a given singly linked list of integers, find and return its length. Do it using an iterative method.

Input format :
        The first line contains an Integer 't' which denotes the number of test cases or queries to be run.
        Then the test cases follow.
        First and the only line of each test case or query contains elements of the singly linked list
        separated by a single space.
        Remember/Consider : While specifying the list elements for input,
        -1 indicates the end of the singly linked list and hence, would never be a list element.
Output format :
        For each test case, print the length of the linked list.
Output for every test case will be printed in a separate line.

Constraints :       1 <= t <= 10^2      0 <= N <= 10^5
Time Limit: 1 sec

Sample Input 1 :    1                                   Sample Output 1 :   7
                    3 4 5 2 6 1 9 -1

Sample Input 2 :    2                                   Sample Output 2 :   8
                    10 76 39 -3 2 9 -23 9 -1                                0
                    -1
'''
# Iterative Solution to find Length of LL
# 1) Initialize count as 0
# 2) Initialize a node pointer, current = head.
# 3) Do following while current is not NULL
#      a) current = current -> next
#      b) count++;
# 4) Return count


from sys import stdin

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# def length(head):           # Finding length of LL using ITERATIVE METHOD
#     count = 0
#     current = head                  # initialize a node pointer, to keep track of node to be traversed
#     while current is not None:      # if current is none means we're at end and it'll return count
#         current = current.next      # go to next of each node one by one
#         count += 1
#     return count


def getCountRec(head):               # Finding length of LL using ITERATIVE METHOD
    if head is None:                # Base case
        return 0
    else:
        return 1 + getCountRec(head.next)

def length(head):
    return getCountRec(head)
    # pass


# Taking Input Using Fast I/O
def takeInput():
    head = None
    tail = None

    print("\nEnter the Elements with space: ")
    # here we're taking input in a single line using list compr. & converting it to a list
    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    # creating a LL of elements taken as i/p.
    # i will run till all the elements in list are traversed upon i.e., length of list(len(datas))
    # below, -1 indicates the end of the singly linked list and hence, would never be a list element
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)    # creatin new node

        if head is None:        # for 1st node when LL is empty
            head = newNode      # make head and tail of every node
            tail = newNode
        else:                   # to update the LL with new elements
            tail.next = newNode
            tail = newNode

        i += 1
    return head

# to print the linked list
def printLinkedList(head):
    while head is not None:
        print(str(head.data) + " -> ", end=" ")
        head = head.next
    print("None")


# main
print("Enter Number of Test Cases: ")
t = int(stdin.readline().rstrip())

while t > 0:
    head = takeInput()

    print("\nLinked List you entered is: ")
    printLinkedList(head)

    print("\nLength of Linked List: ")
    print(length(head))

    t -= 1