from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length(head):                   # Finding length of LL using ITERATIVE METHOD
    count = 0
    current = head                  # initialize a node pointer, to keep track of node to be traversed
    while current is not None:      # if current is none means we're at end and it'll return count
        current = current.next      # go to next of each node one by one
        count += 1
    return count

#ITERATIVE SOLUTION
# def insertAtIthPositionIteratively(head, i, data):      # function to insert in LL at ith position
#
#     if i<0 or i>length(head):   # first calculate length of LL
#         return head         # we can't insert a element if index doesn't lie in range of length of LL
#
#     count = 0               # pointer to traverse array till index is reached
#     prev = 0                # this'll point towards previous node
#     curr = head             # this'll pt. towards current node which is being traversed
#                             # we need to insert our data b/w prev & curr nodes
#     while count < i:        # first we have to go to that index at which we want to insert
#         prev = curr         # swapping address pointers: chalte jao till we reach our desired index
#         curr = curr.next
#         count += 1          # now count will become = to i, as we've reached our index
#     newNode = Node(data)    # create a new Node using 'Node Class'
#     if prev is not None:    # means we're inserting in b/w or at end of LL
#         prev.next = newNode # link the new node with next of previous node
#     else:                   # if we're inserting at 0th(starting) position, make new node as head
#         head = newNode
#     newNode.next = curr     # link new node with data of next current node
#
#     return head             # return head so we can traverse the list



#RECURSIVE SOLUTION
def insertAtIthPositionRecursively(head, i, data):      # function to insert in LL at ith position

    if i<0:
        return head
    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    if head is None:
        return None
    smallHead =  insertAtIthPositionRecursively(head.next, i-1, data)
    head.next = smallHead
    pass


#Taking Input Using Fast I/O
def takeInput() :
    head = None
    tail = None
    print("\nEnter the Elements: ")
    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
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
def printLinkedList(head) :
    while head is not None :
        print(str(head.data) + " -> ", end = " ")
        head = head.next
    print("None")
    # print()


#main
print("Enter the Number of Test Cases: ")
t = int(stdin.readline().rstrip())

while t > 0 :

    head = takeInput()
    print("\nYour LL is: ")
    printLinkedList(head)

    print("\nEnter the Index Position:")
    i = int(stdin.readline().rstrip())

    print(f"\nEnter the Data to insert at {i}th position:")
    data = int(stdin.readline().rstrip())

    # r = (insertAtIthPositionIteratively(head, i, data))
    r = (insertAtIthPositionRecursively(head, i, data))
    print("\nAfter Insertion new Linked List:",)
    printLinkedList(r)


    t -= 1