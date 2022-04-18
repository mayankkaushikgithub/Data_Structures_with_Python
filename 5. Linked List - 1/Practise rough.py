# class Node:
#     def __init__(self, data):       # every node consists of data & next(reference of next ele)
#         self. data = data
#         self.next = None            # at first 'a' didn't store any reference
# a = Node(13)
# b = Node(15)
# a.next = b                          # now a's next store the reference of b's data
# print(a.data)
# print(b.data)
# print(a.next.data)          # this will first go to a.next(which stores reference of b) then print b.data
# print(a.next)               # this shows reference of next element
# print(b)                    # this prints ref. of b, as b itself is next element so address is same in memory
# print(b.next.data)        # this will give error as b is last element it doesn't store ref. of any other ele.



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def printLL(head):                      # data of node2 i.e., 20
#     while head is not None:             # this'll run till we have value in head
#         print(head.data,end=" ")        # 1st it'll print data of node2 as node2 is passed as argument
#         head = head.next                # now head is updated with address of next element
#
# node1 = Node(10)        # first node1, node2 objects are created using class init()
# node2 = Node(20)
# node2.next = node1      # node2 points to address of node1
# printLL(node2)          # it'll go to printLL()



# class Node:         # same as above
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def printLL(head):
#     while head is not None:
#         print(head.data,end=" ")
#         head = head.next
#
# node1 = Node(10)
# node2 = Node(20)
# node3 = Node(30)
# node4 = Node(40)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# printLL(node2)



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# def printLL(head):          # now as the data in heads of node1,2 is updated, it'll print updated data
#     while head is not None:
#         print(head.data,end=" ")
#         head = head.next
# def increment(head):        # this fun() will update data in nodes
#      temp = head
#      while temp is not None:
#         temp.data +=1
#         temp = temp.next
#
# node1 = Node(10)        # first create both the nodes
# node2 = Node(20)
# node1.next = node2      # add reference of node2's address to 'next' of 'node1'
# increment(node1)
# printLL(node1)


# Q. What will be the time complexity of searching an element in the linked list ?
# A. O(n)


# Q. Consider the Singly linked list having n elements.
#    What will be the time taken to add an node at the end of linked list
#    if is initially pointing to first node of the list. That is only head is given to you.
# A. O(n)


# Q. There is reference (or pointer) to first Node of the Linked List,
#    then time required to insert element to second position is __________.
#    Indexing starts from 0.
# A. O(1)


# Q. Given an unsorted singly Linked List, suppose you have reference (or pointer) to its head node only,
#    which of the following operation can be implemented in O(1) time?
#    i)   Insertion at the front of the linked list
#     i)  Insertion at the end of the linked list
#    iii) Deletion of the last node of the linked list
#    iv)  Deletion of the front node of the linked list
# A. (i) and (iv)


# Q. Given an unsorted singly Linked List, suppose you have references (or pointer)
#    to its head and tail nodes, which of the following operation can be implemented in O(1) time?
#       i)   Insertion at the front of the linked list
#       ii)  Insertion at the end of the linked list
#       iii) Deletion of the last node of the linked list
#       iv)  Deletion of the front node of the linked list
# A. (i), (ii) and (iv)