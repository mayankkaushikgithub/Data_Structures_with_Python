from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def nodeToRootPath(root, s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return l

    leftOutput = nodeToRootPath(root.left, s)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput

    rightOutput = nodeToRootPath(root.right, s)
    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None

#---------------------------------------------------------#




def printLevelWise(root):                                     # OUTPUT FUNCTION
    if root is None:
        return None
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        # print("\nRoot")
        print(str(currentNode.data) + ": ", end="")
        if currentNode.left != None:
            # print("Left:")
            q.put(currentNode.left)
            print("L:",str(currentNode.left.data) + ", ", end="")
        else:
            print("L:-1,", end="")
        if  currentNode.right != None:
            # print("\nRight:")
            q.put(currentNode.right)
            print("R:",str(currentNode.right.data), end="")
        else:
            print(" R:-1", end="")
        print()

def takeLevelWiseTreeInput():                           # INPUT FUNCTION
    q = queue.Queue()
    print("Enter Root: ")
    rootData = int(input())                             # take the root of main/sub tree
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)                     # make a node out of this data
    q.put(root)                                         # put this data in queue now we we'll perform on this data until -1
    while not(q.empty()):                               # till all the data is cleared from queue
        currentNode = q.get()                           # take out the first data (FIFO)
        print("Enter Left Child of", currentNode.data)       # take its child first as it comes first
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)   # make node out of this data
            currentNode.left = leftChild                # join it with ptr of current node
            q.put(leftChild)                            # add it to queue
        print("Enter Right Child of", currentNode.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            currentNode.right = rightChild
            q.put(rightChild)
    return root


# input tree: 1 2 3 4 6 5 9 7 8
root = takeLevelWiseTreeInput()

print("Structure of Tree you entered is: ")
printLevelWise(root)

res = nodeToRootPath(root, 5)

print(res)