'''
Diameter Of Binary Tree

For a given Binary of type integer, find and return the ‘Diameter’.

Diameter of a Tree can be defined as the maximum distance between two leaf nodes.
Here, the distance is measured in terms of the total number of nodes present along the path of the two leaf nodes,
including both the leaves.
Example:

                        2
                      /   \
                    4      5
                   /        \
                  6          7
                /  \        /  \
              20   30      80   90
                   /        \
                 8           9

The maximum distance can be seen between the leaf nodes 8 and 9.
The distance is 9 as there are a total of nine nodes along the longest path from 8 to 9(inclusive of both).
Hence the diameter according to the definition will be 9.

Input Format:
        The first and the only line of input will contain the node data, all separated by a single space.
        Since -1 is used as an indication whether the left or right node data exist for root,
        it will not be a part of the node data.
Output Format:
        The only line of output prints an integer, representing the diameter of the tree.

Note:   You are not required to print anything explicitly. It has already been taken care of.
Constraints:    1 <= N <= 10^5      Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Sample Input 1: 2 4 5 6 -1 -1 7 20 30 80 90 -1 -1 8 -1 -1 9 -1 -1 -1 -1 -1 -1                   Sample Output 1:9

Sample Input 2: 1 2 3 4 5 6 7 -1 -1 -1 -1 -1 -1 -1 -1                                           Sample Output 2:5

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


'''The diameter of a tree (aka width) is the number of nodes on the longest path between two end nodes. '''

#--------------------------- METHOD - 1 -----------------------------------------------# (SLOW) O(n^2)
# def height(root):
#     if root is None:                        # Base Case (if no node present height is 0)
#         return 0
#     # If tree is not empty then height = 1 + max of left height and right heights
#     return 1 + max(height(root.left), height(root.right))
#
# def diameterOfBinaryTree(root):
#     if root == None:
#         return 0
#     lh = height(root.left)                        # calculating height of sub - trees
#     rh = height(root.right)
#     ld = diameterOfBinaryTree(root.left)          # calculating diameter of sub - trees
#     rd = diameterOfBinaryTree(root.right)
                                                    # Return max of the following tree:
    # return max(lh + rh + 1, max(ld, rd))          # 1) Diameter of left subtree
                                                    # 2) Diameter of right subtree
                                                    # 3) Height of left subtree + height of right subtree +1
#--------------------------------------------------------------------------------------#



#--------------------------- METHOD - 2 (BETTER) --------------------------------------# (FASTER) O(n^2)

def getDiameter(root, diameter):                                # make seprate function as we want only one value
                                                                # to be returned but this fun. returns 2

    if root == None:                                                        # Base Case: Tree is Empty
        return 0, diameter

    leftHeight, leftDiameter = getDiameter(root.left, diameter)             # ask for height & diameter in same call
    rightHeight, rightDiameter = getDiameter(root.right, diameter)          # height & diameter of sub-trees

    d = max(leftHeight + rightHeight + 1, max(leftDiameter, rightDiameter))

    return max(leftHeight, rightHeight)+1, d                                # return max height of sub tree

def diameterOfBinaryTree(root):
    d = 0
    return getDiameter(root, d)[1]

#------------------------------------------------------------------------------------#




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
    if root == None:
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

print(diameterOfBinaryTree(root))