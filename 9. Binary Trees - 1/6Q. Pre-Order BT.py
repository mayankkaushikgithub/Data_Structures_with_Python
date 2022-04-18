'''
Preorder Binary Tree        Order: (ROOT -> LEFT -> RIGHT)

For a given Binary Tree of integers, print the pre-order traversal.

Input Format:
    The first and the only line of input will contain the nodes data, all separated by a single space.
    Since -1 is used as an indication whether the left or right node data exist for root,
    it will not be a part of the node data.
Output Format:
    The only line of output prints the pre-order traversal of the given binary tree.

Constraints:    1 <= N <= 10^6      Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Sample Input 1:     5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1               Sample Ouptut 1:    5 6 2 3 9 10

Sample Input 2:     1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1           Sample Ouptut 2:    1 2 4 5 3 6 7

'''

from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(root):         # Pre-Order: (ROOT -> LEFT -> RIGHT)
# Root takes care of its children before taking care of its children
    if root == None:
        return

    print(root.data, end=" ")
    # root.data

    if root.left != None:
        # print(root.left.data)
        root.left.data
    if root.right != None:
        # print(root.right.data)
        root.right.data

    # print()
    preOrder(root.left)
    preOrder(root.right)




# Your code goes here


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

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
preOrder(root)