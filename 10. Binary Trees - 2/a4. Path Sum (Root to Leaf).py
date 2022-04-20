'''
Path Sum Root to Leaf

For a given Binary Tree of type integer and a number K, print out all root-to-leaf paths
where the sum of all the node data along the path is equal to K.

Example:
                        2
                      /   \
                    3      9
                   / \      \
                  4   8      2
                /           /
              4           6

If you see in the above-depicted picture of Binary Tree, we see that there are a total of two paths,
starting from the root and ending at the leaves which sum up to a value of K = 13.

The paths are:
a. 2 3 4 4
b. 2 3 8

One thing to note here is, there is another path in the right sub-tree in reference to the root,
which sums up to 13 but since it doesn't end at the leaf, we discard it.
The path is: 2 9 2(not a leaf)

Input Format:
        The first line of input will contain the node data, all separated by a single space.
        Since -1 is used as an indication whether the left or right node data exist for root,
        it will not be a part of the node data.
        The second line of input contains an integer value K.
Output Format:
        Lines equal to the total number of paths will be printed. All the node data in every path will be printed
        in a linear fashion taken in the order they appear from top to down bottom in the tree.
        A single space will separate them all.

Constriants:    1 <= N <= 10^5  0 <= K <= 10^8  Where N is the total number of nodes in the binary tree.
Time Limit: 1 second

Sample Input 1:     2 3 9 4 8 -1 2 4 -1 -1 -1 6 -1 -1 -1 -1 -1                       Sample Output 1:   2 3 4 4
                    13                                                                                  2 3 8

Sample Input 2:     5 6 7 2 3 -1 1 -1 -1 -1 9 -1 -1 -1 -1                             Sample Output 2:   5 6 2
                    13                                                                                   5 7 1

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


# This function prints all paths that have sum k
def printPathsUtil(curr_node, sum, sum_so_far, path):

    if (not curr_node):                                     # Base Case     # empty node
        return
    sum_so_far += curr_node.data                            # update the sum

    path.append(curr_node.data)                             # add current node to the path

    if (sum_so_far == sum):                                 # print the required path
        print("Path found:", end=" ")
        for i in range(len(path)):
            print(path[i], end=" ")
        print()

    if (curr_node.left != None):                            # if left child exists
        printPathsUtil(curr_node.left, sum, sum_so_far, path)

    if (curr_node.right != None):                           # if right child exists
        printPathsUtil(curr_node.right, sum, sum_so_far, path)

    path.pop(-1)                                            # Remove the current element from the path


def rootToLeafPathsSumToK(root, k):
    path = []
    printPathsUtil(root, k, 0, path)









# Your code goes here


# Taking level-order input using fast I/O method
def takeInput():
    print("Enter the Nodes of Tree:")
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

print("\nEnter the Sum: ")
k = int(stdin.readline().strip())
rootToLeafPathsSumToK(root, k)