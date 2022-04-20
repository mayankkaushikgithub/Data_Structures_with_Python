'''
Minimum and Maximum in the Binary Tree

For a given a Binary Tree of type integer, find and return the minimum and the maximum data values.
Return the output as an object of Pair class, which is already created.

Note:   All the node data will be unique and hence there will always exist a minimum and maximum node data.

Input Format:
        The first and the only line of input will contain the node data, all separated by a single space.
        Since -1 is used as an indication whether the left or right node data exist for root,
        it will not be a part of the node data.
Output Format:
        The only line of output prints two integers denoting the minimum and the maximum data values respectively.
        A single line will separate them both.

Constraints:    2 <= N <= 10^5      Where N is the total number of nodes in the binary tree.
Time Limit: 1 sec

Sample Input 1:     8 3 10 1 6 -1 14 -1 -1 4 7 13 -1 -1 -1 -1 -1 -1 -1                      Sample Output 1:    1 14

Sample Input 2:     10 20 60 -1 -1 3 50 -1 -1 -1 -1                                         Sample Output 2:    3 60

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


# Representation of the Pair Class
class Pair:

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum


def getMinimum(root):                     # Solution 1
    if root == None:
        return 2                          # 2 <= N <= 10^5 is constraint that's why we're returning 2
    res = root.data
    lres = getMinimum(root.left)
    rres = getMinimum(root.right)
    return min(min(lres, rres), res)
def getMaximum(root):
    if root == None:
        return -1
    res = root.data
    lres = getMaximum(root.left)
    rres = getMaximum(root.right)
    return max(max(lres, rres), res)
def getMinAndMax(root):
    if root == None:
        return -1
    mini = getMinimum(root)
    maxi = getMaximum(root)
    pair = Pair(mini, maxi)
    return pair

def getMinAndMax(root):                                         # Solution 2 (not complete)
    if root == None:
        return 2, 0
    ls, lb = getMinAndMax(root.left)
    rs, rb = getMinAndMax(root.right)
    small = min(min(ls, rs), root.data)
    big = max(max(lb, rb), root.data)

    pair = Pair(small, big)
    return pair





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

pair = getMinAndMax(root)
print(str(str(pair.minimum) + " " + str(pair.maximum)))