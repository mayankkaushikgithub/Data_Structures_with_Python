'''
Postorder Binary Tree       # Post-Order: (LEFT -> RIGHT -> ROOT)

For a given Binary Tree of integers, print the post-order traversal.
Input Format:
        The first and the only line of input will contain the node data, all separated by a single space.
        Since -1 is used as an indication whether the left or right node data exist for root,
        it will not be a part of the node data.
Output Format:
        The only line of output prints the post-order traversal of the given binary tree.

Constraints:        1 <= N <= 10^6      Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Sample Input 1:     1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1                    Sample Output 1:   4 5 2 6 7 3 1

Sample Input 2:     5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1                         Sample Output 1:   2 9 3 6 10 5

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


def preOrder(root):                             # Post-Order: (LEFT -> RIGHT -> ROOT)

    if root == None:
        return

    preOrder(root.left)                         # 1. go till the end node of left side tree
    if root.left != None:
        # print(root.left.data, end=" ")
        root.left.data

    preOrder(root.right)                        # 2. go till the end node of right side tree
    if root.right != None:
        # print(root.right.data, end=" ")
        root.right.data


    print(root.data, end=" ")                   # 3. Visit the root



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