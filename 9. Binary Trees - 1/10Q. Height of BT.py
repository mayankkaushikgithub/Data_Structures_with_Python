'''
Height Of Tree

For a given Binary Tree of integers, find and return the height of the tree.
Example:
                        10
                      /   \
                    20    30
                   /  \
                 40   50

Height of the given tree is 3.

Height is defined as the total number of nodes along the longest path from the root to any of the leaf node.

Input Format:
        The first and the only line of input will contain the node data, all separated by a single space.
        Since -1 is used as an indication whether the left or right node data exist for root,
        it will not be a part of the node data.
Output Format:
        The first and the only line of output prints the height of the given binary tree.

Note:   You are not required to print anything explicitly. It has already been taken care of.
Constraints:    0 <= N <= 10^5      Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Sample Input 1:     10 20 30 40 50 -1 -1 -1 -1 -1 -1                            Sample Output 1:    3

Sample Input 2:     3 -1 -1                                                    Sample Output 2:    1

'''

'''

THEORY:
The height of the binary tree is the longest path from root node to any leaf node in the tree.
In a binary tree, a node can have maximum two children.

Calculating minimum and maximum height from the number of nodes –
If there are n nodes in a binary search tree, 
Maximum Height of the binary search tree is (n-1) and Minimum Height is floor(log2n).

Calculating minimum and maximum number of nodes from height –
If binary search tree has height h, Minimum number of nodes is h+1 (in case of left skewed and right skewed binary search tree).
If binary search tree has height h, Maximum number of nodes will be when all levels are completely full. 
Total number of nodes will be 2^0 + 2^1 + …. 2^h = 2^(h+1)-1.

'''
# The maximum and minimum number of nodes in a binary tree of height 6 are: 63 & 6 respectively





from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# def height(root):                           # METHOD - 2
#     if root is None:                        # Base Case (if no node present height is 0)
#         return 0
#     leftHeight = height(root.left)          # count the nodes of left side
#     rightHeight = height(root.right)        # count the nodes of right side
#     if leftHeight > rightHeight:            # whichever has more nodes will give height of tree
#         return 1 + leftHeight               # +1 is for root node
#     return 1 + rightHeight


def height(root):                             # METHOD - 1
    if root == None:
        return
# If tree is not empty then height = 1 + max of left height and right heights
    return 1 + max(height(root.left), height(root.right))


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


# Main
root = takeInput()

h = height(root)
print(h)