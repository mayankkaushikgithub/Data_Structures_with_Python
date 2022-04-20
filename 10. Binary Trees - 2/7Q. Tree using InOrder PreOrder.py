'''
Construct Tree Using Inorder and Preorder
Send Feedback
For a given preorder and inorder traversal of a Binary Tree of type integer stored in an array/list,
create the binary tree using the given two arrays/lists. You just need to construct the tree and return the root.

Note:   Assume that the Binary Tree contains only unique elements.

Input Format:
        The first line of input contains an integer N denoting the size of the list/array.
        It can also be said that N is the total number of nodes the binary tree would have.

        The second line of input contains N integers, all separated by a single space.
        It represents the preorder-traversal of the binary tree.

        The third line of input contains N integers, all separated by a single space.
        It represents the inorder-traversal of the binary tree.
Output Format:
        The given input tree will be printed in a level order fashion where each level will be printed on a new line.
        Elements on every level will be printed in a linear fashion. A single space will separate them.

Constraints:        1 <= N <= 10^4      Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Sample Input 1:     7
                    1 2 4 5 3 6 7
                    4 2 5 1 6 3 7
Sample Output 1:    1
                    2 3
                    4 5 6 7

Sample Input 2:     6
                    5 6 2 3 9 10
                    2 6 3 9 5 10
Sample Output 2:    5
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


def buildTree(preOrder, inOrder, n):

    if len(preOrder) == 0:
        return None

    # root of the binary tree would be the same as the first element in the preorder array.
    rootData = preOrder[0]
    root = BinaryTreeNode(rootData)                         # make node out of this data
    rootIndexInInOder = -1


    for i in range(len(inOrder)):                           # search for position of this ele in InOrder list
        if inOrder[i] == rootData :
            rootIndexInInOder = i
            break
    if rootIndexInInOder == -1:
        return None


    # If found, all the node values to the left of that root node’s value would form it’s left subtree,
    # while all the node values to the right of that root node’s value would form it’s right subtree.
    leftInorder = inOrder[0 : rootIndexInInOder]            # make size of left subTree(LST) from i
    rightInorder = inOrder[rootIndexInInOder+1: ]           # make size of right subTree


    lenLeftSubTree = len(leftInorder)                       # use InOrder LST to find preOrder Index size


    leftPreorder = preOrder[1 : lenLeftSubTree+1]           # find left & right preOrder
    rightPreorder = preOrder[lenLeftSubTree+1 : ]

    n = len((leftPreorder))
    leftChild = buildTree(leftPreorder, leftInorder, n)             # call recursion
    rightChild = buildTree(rightPreorder, rightInorder, n)

    root.left = leftChild                                   # link the LST & RST with main Root Node
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
    print("Enter Total Number of Nodes of Tree: ")
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    print("\nEnter Nodes in Pre-Order(Root->LST->RST")
    preOrder = list(map(int, stdin.readline().strip().split(" ")))

    print("\nEnter Nodes in In-Order(LST->Root->RST")
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


# Main
preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)