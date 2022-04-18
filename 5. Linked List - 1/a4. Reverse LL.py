'''
Print Reverse LinkedList
Send Feedback
You have been given a singly linked list of integers. Write a function to print the list in a reverse order.
To explain it further, you need to start printing the data from the tail and move towards the head of the list, printing the head data at the end.
Note :
You can’t change any of the pointers in the linked list, just print it in the reverse order.
 Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.

The first and the only line of each test case or query contains the elements of the singly linked list separated by a single space.
Remember/Constraints :
While specifying the list elements for input, -1 indicates the end of the singly linked list and hence, would never be a list element.
Output format :
For each test case, print the singly linked list of integers in a reverse fashion, in a row, separated by a single space.

Output for every test case will be printed in a seperate line.
 Constraints :
1 <= t <= 10^2
0 <= M <= 10^3
Time Limit: 1sec

Where 'M' is the size of the singly linked list.
Sample Input 1 :
1
1 2 3 4 5 -1
Sample Output 1 :
5 4 3 2 1
Sample Input 2 :
2
1 2 3 -1
10 20 30 40 50 -1
Sample Output 2 :
3 2 1
50 40 30 20 10
'''




from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def printReverse(head) :

    if head is None:
        return None
    if head.next is None:
        return head

    prev_node = None                 # Initialize three pointers prev as NULL, curr as head and next as NULL.
    curr_node = head
    next_node = None

    while curr_node is not None:

        next_node = curr_node.next        # make next of curr_node as next_node
        curr_node.next = prev_node        # This is where actual reversing happens. here we reverse the pointer of curr_node.
        # Earlier it was pointing to 'next node' now it'll point to 'previous_node'

        prev_node = curr_node             # Move prev and curr one step forward
        curr_node = next_node

        head = prev_node

    return head






#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None

    print("\nEnter the Values of Nodes: ")
    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head


#to print the linked list
def printLinkedList(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()

#main
print("Enter Total Number of Test Cases: ")
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()

    print("\nReversed Linked List: ")
    r = printReverse(head)
    # print()
    printLinkedList(r)

    t -= 1