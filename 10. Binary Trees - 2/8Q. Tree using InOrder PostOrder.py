'''
Construct Tree Using Inorder and PostOrder

For a given postorder and inorder traversal of a Binary Tree of type integer stored in an array/list,
create the binary tree using the given two arrays/lists. You just need to construct the tree and return the root.

Note:   Assume that the Binary Tree contains only unique elements.

Input Format:
        The first line of input contains an integer N denoting the size of the list/array.
        It can also be said that N is the total number of nodes the binary tree would have.

        The second line of input contains N integers, all separated by a single space.
        It represents the Postorder-traversal of the binary tree.

        The third line of input contains N integers, all separated by a single space.
        It represents the inorder-traversal of the binary tree.
Output Format:
        The given input tree will be printed in a level order fashion where each level will be printed on a new line.
        Elements on every level will be printed in a linear fashion. A single space will separate them.

Constraints:    1 <= N <= 10^4      Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Sample Input 1: 7
                4 5 2 6 7 3 1
                4 2 5 1 6 3 7
Sample Output 1:
                1
                2 3
                4 5 6 7

Sample Input 2: 6
                2 9 3 6 10 5
                2 6 3 9 5 10
Sample Output 2:
                5
                6 10
                2 3
                9
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


def buildTree(postOrder, inOrder, n=0):

    if len(postOrder) == 0:
        return None

    rootData = postOrder[-1]                            # in postOrder root is at last
    root = BinaryTreeNode(rootData)

    rootIndexInorder = 0
    for i in range(len(inOrder)):                       # search the index of root in InOrder
        if inOrder[i] == rootData:
            rootIndexInorder = i
            # print(rootIndexInorder)
            break
    if rootIndexInorder == -1:
        return None

    leftInorder = inOrder[0 : rootIndexInorder]                 # ele on left of index
    rightInorder = inOrder[rootIndexInorder+1 : ]               # ele on right of index

    leftPostOrder = postOrder[ : rootIndexInorder]
    rightPostOrder = postOrder[rootIndexInorder : -1]           # reverse as ele is present at last

#From previous 2 steps construct the left and right subtree and link it to root.left and root.right respectively.
    n = len(leftPostOrder)
    leftChild = buildTree(leftPostOrder, leftInorder, n)
    rightChild = buildTree(rightPostOrder, rightInorder, n)


    root.left = leftChild
    root.right = rightChild
    return root


# Your code goes here


'''-------------------------- Utility Functions --------------------------'''


def printLevelWise(root):
    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)

        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


# Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)