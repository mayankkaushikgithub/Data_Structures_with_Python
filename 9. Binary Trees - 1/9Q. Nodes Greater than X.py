'''
Nodes Greater Than X

For a given a binary tree of integers and an integer X, find and return the total number of nodes
of the given binary tree which are having data greater than X.

Input Format:
        The first line of input will contain the node data, all separated by a single space.
        Since -1 is used as an indication whether the left or right node data exist for root,
        it will not be a part of the node data.
        The second line of input contains an integer, denoting the value of X.

Note:   You are not required to print anything explicitly. It has already been taken care of.

Output Format:
        The only line of output prints the total number of nodes where the node data is greater than X.

Constraints:        1 <= N <= 10^5      Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Sample Input 1:     1 4 2 3 -1 -1 -1                                   Sample Output 1:    2
                    2
Explanation for Sample Input 1:
Out of the four nodes of the given binary tree, [3, 4] are the node data that are greater than X = 2.

Sample Input 2:     5 6 10 2 3 -1 -1 -1 -1 -1 9 -1 -1                   Sample Output 2:    3
                    5
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


def countNodesGreaterThanX(root, x):

    if root is None:
        return 0

    countLeft = countNodesGreaterThanX(root.left, x)
    countRight = countNodesGreaterThanX(root.right, x)

    if root.data > x:
        return countLeft + countRight

    return countLeft + countRight + 1




# Your code goes here


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))    # takes nodes i/p & convert them in list
    start = 0                                       # start is to traverse on nodes, start 0 will give root node, so on

    length = len(levelOrder)
    # if length <= 0 or levelOrder[0] == -1:
    #     return None

    root = BinaryTreeNode(levelOrder[start])                # make new node (initially make it root)
    start += 1

    q = queue.Queue()                                       # using queue class to push/pop nodes
    q.put(root)                                             # insert root in queue ?

    while not q.empty():
        currentNode = q.get()                               # put the top most node in currentNode

        leftChild = levelOrder[start]                       # put next node in leftChild
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
print("Enter the Nodes of Tree: ")
root = takeInput()

print("\nEnter the Node to search for: ")
x = int(stdin.readline().strip())

count = countNodesGreaterThanX(root, x)

print(f"\nNode(s) Greater than {x} is/are: ")
print(count)