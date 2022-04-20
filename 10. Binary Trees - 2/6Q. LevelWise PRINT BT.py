'''
Print Levelwise
Send Feedback
For a given a Binary Tree of type integer, print the complete information of every node,
when traversed in a level-order fashion.
To print the information of a node with data D, you need to follow the exact format :

           D:L:X,R:Y

Where D is the data of a node present in the binary tree.
X and Y are the values of the left(L) and right(R) child of the node.
Print -1 if the child doesn't exist.
Example:
                         1
                      /    \
                    2       3
                   /       / \
                  4       5   6
                   \
                    7

For the above depicted Binary Tree, the level order travel will be printed as followed:

1:L:2,R:3
2:L:4:,R:-1
3:L:5:,R:6
4:L:-1:,R:7
5:L:-1:,R:-1
6:L:-1:,R:-1
7:L:-1:,R:-1

Note: There is no space in between while printing the information for each node.

Input Format:
        The first and the only line of input will contain the node data, all separated by a single space.
        Since -1 is used as an indication whether the left or right node data exist for root,
        it will not be a part of the node data.
Output Format:
        Information of all the nodes in the Binary Tree will be printed on a different line
        where each node will follow a format of D:L:X,R:Y, without any spaces in between.

Constraints:    1 <= N <= 10^5  Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec
'''

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



#---------------------------------------------------------#
def printLevelWise(root):                                                           # MY SOLUTION
    if root is None:
        return None

    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        # print("\nRoot")
        print(str(currentNode.data) + ": ", end="")

        if currentNode.left != None:
            # print("Left:")
            q.put(currentNode.left)
            print("L:",str(currentNode.left.data) + ", ", end="")
        else:
            print("L:-1,", end="")

        if  currentNode.right != None:
            # print("\nRight:")
            q.put(currentNode.right)
            print("R:",str(currentNode.right.data), end="")
        else:
            print(" R:-1", end="")

        print()


# def printLevelWise(root):                                                               # CODING NINJA SOLUTION
#     if root is None:
#         return None
#     q = queue.Queue()
#     q.put(root)
#     while not q.empty():
#         rootData = q.get()
#
#         if rootData.left is None and rootData.right is None:
#             pass
#         elif rootData.left is None and rootData.right is not None:
#             q.put(rootData.right)
#         elif rootData.left is not None and rootData.right is None:
#             q.put(rootData.left)
#         else:
#             q.put(rootData.left)
#             q.put(rootData.right)
#
#         print(str(rootData.data) + ":", end="")
#         if rootData.left is None:
#             print("L:-1,", end="")
#         else:
#             print("L:" + str(rootData.left.data) + ",", end="")
#         if rootData.right is None:
#             print("R:-1", end="")
#         else:
#             print("R:" + str(rootData.right.data), end="")
#         print()
#     # Your code goes here
#---------------------------------------------------------#





# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    if length == 1:
        return None

    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


# Main
root = takeInput()
printLevelWise(root)