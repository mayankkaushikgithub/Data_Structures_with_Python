'''
Print nodes at distance k from node

You are given a Binary Tree of type integer, a target node, and an integer value K.
Print the data of all nodes that have a distance K from the target node.
The order in which they would be printed will not matter.

Example:
For a given input tree(refer to the image below):
1. Target Node: 5
2. K = 2
                         3
                      /    \
                    5       1
                   / \     / \
                  6   2   0   8
                     / \
                    7   4
Starting from the target node 5, the nodes at distance K are 7 4 and 1.

Input Format:
    The first line of input will contain the node data, all separated by a single space.
    Since -1 is used as an indication whether the left or right node data exist for root, it will not be a part of the node data.
    The second line of input contains two integers separated by a single space, representing the value of the target node and K, respectively.
Output Format:
    All the node data at distance K from the target node will be printed on a new line.
    The order in which the data is printed doesn't matter.
Constraints:    1 <= N <= 10^5  Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Sample Input 1:     5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1                   Sample Output 1:    9
                    3 1                                                                     6

Sample Input 2:     1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1               Sample Output 2:    4
                    3 3                                                                     5
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







# # Recursive function to print all the nodes at distance k
# # int the tree(or subtree) rooted with given root. See
# def printkDistanceNodeDown(root, k):
#     # Base Case
#     if root is None or k < 0:
#         return
#
#     # If we reach a k distant node, print it
#     if k == 0:
#         print(root.data)
#         return
#
#     # Recur for left and right subtee
#     printkDistanceNodeDown(root.left, k - 1)
#     printkDistanceNodeDown(root.right, k - 1)
#
#
# # Prints all nodes at distance k from a given target node
# # The k distant nodes may be upward or downward. This function
# # returns distance of root from target node, it returns -1
# # if target node is not present in tree rooted with root
# def printkDistanceNode(root, target, k):
#     # Base Case 1 : IF tree is empty return -1
#     if root is None:
#         return -1
#
#     # If target is same as root. Use the downward function
#     # to print all nodes at distance k in subtree rooted with
#     # target or root
#     if root == target:
#         printkDistanceNodeDown(root, k)
#         return 0
#
#     # Recur for left subtree
#     dl = printkDistanceNode(root.left, target, k)
#
#     # Check if target node was found in left subtree
#     if dl != -1:
#
#         # If root is at distance k from target, print root
#         # Note: dl is distance of root's left child
#         # from target
#         if dl + 1 == k:
#             print(root.data)
#
#         # Else go to right subtreee and print all k-dl-2
#         # distant nodes
#         # Note: that the right child is 2 edges away from
#         # left chlid
#         else:
#             printkDistanceNodeDown(root.right, k - dl - 2)
#
#         # Add 1 to the distance and return value for
#         # for parent calls
#         return 1 + dl
#
#     # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE
#     # Note that we reach here only when node was not found
#     # in left subtree
#     dr = printkDistanceNode(root.right, target, k)
#     if dr != -1:
#         if (dr + 1 == k):
#             print(root.data)
#         else:
#             printkDistanceNodeDown(root.left, k - dr - 2)
#         return 1 + dr
#
#     # If target was neither present in left nor in right subtree
#     return -1





















# Your code goes here


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


def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

# nodesAtDistanceK(root, target, k)
printkDistanceNode(root, target, k)