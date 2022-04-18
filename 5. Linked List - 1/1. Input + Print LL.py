'''
Like arrays, Linked List is a linear data structure.
Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# def takeInput():                            # METHOD-1 it takes time O(n^2) as we've to traverse till n-1 ele for n ele
#     inputList = [int(ele) for ele in input().split()] # taking list as input using one line list comprehension
#     head = None                             # initially head will not point to any other element
#     for currData in inputList:
#         if currData == -1:                  # if nothing in list break
#             break
#         newNode = Node(currData)            # whenever a new ele comes, a new Node is created
#         if head is None:                    # this'll execute at the beginning when there's no ele in list
#             head = newNode                  # make first ele in list as 1st node
#         else:
#             curr = head                     # don't perform operation on head, make another ptr to traverse  on nodes
#             while curr.next is not None:    # till current point to address of another node
#                 curr = curr.next            # if curr points to address of another node, update curr with next node
#             curr.next = newNode             # if curr stores None(in next), assign 'newNode' address to its next
#     return head                             # now we've head of LL we can do anything with it


def takeInput():                              # METHOD-2 (more efficient)
    inputList = [int(ele) for ele in input().split()]

    head = None
    tail = None
    for currentData in inputList:
        if currentData == -1:
            break
        newNode = Node(currentData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


def printLL(head):
    while head is not None:                 # if there's data in head of node
        print(str(head.data) + " -> ", end="")
        head = head.next                    # move head to next node's address
    print("None")
    return


head = takeInput()  # this head is main(point to head of LL) we can call as many printLL() we want to print,
printLL(head)       # we'll pass the head of LL to printLL(), this head(is copy to main head)is local to this fun itself