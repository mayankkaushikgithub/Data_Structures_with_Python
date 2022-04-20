from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



#------------------ SOLUTION - 1 ------------------------------

# def minTree(root):
#     if root == None:
#         return -100000
#     leftmin = minTree(root.left)
#     rightmin = minTree(root.right)
#     return min(leftmin, rightmin, root.data)
#
# def maxTree(root):
#     if root == None:
#         return 100000
#     leftmax = maxTree(root.left)
#     rightmax = maxTree(root.right)
#     return max(leftmax, rightmax, root.data)
#
# def isBST(root):
#     if root == None:
#         return
#     leftMax = maxTree(root.left)
#     rightMin = maxTree(root.right)
#     if root.data > rightMin or root.data <= leftMax:
#         return False # means it is not a BST
#
#     isLeftBST = isBST(root.left)
#     isRightBST = isBST(root.right)
#     return isLeftBST and isRightBST



#-------------------------SOLUTION - 2 (Better) -----------------

# Time Complexity: T(n) = 2T(n/2) + k = O(n)
# def isBST2(root):
#     if root == None:
#         return 100000, -100000, True
#     leftMin, leftMax, isLeftBST = isBST2(root.left)
#     rightMin, rightMax, isRightBST2 = isBST2(root.right)
#
#     minimum = min(leftMin, rightMin, root.data)
#     maximum = max(leftMax, rightMax, root.data)
#
#     isTreeBST = True
#     if root.data <= leftMax or root.data > rightMin:
#         isTreeBST = False
#
#     if not(isLeftBST) or not(isRightBST2):
#         isTreeBST = False
#
#     return minimum, maximum, isTreeBST



#---------------- SOLUTION - 3 -------------------------

def isBST3(root, min_range, max_range):
    if root == None:
        return True

    if root.data < min_range or root.data > max_range:
        return False

    isLeftWithinConstraint = isBST3(root.left, min_range, root.data-1)
    isRightWithinConstraint = isBST3(root.right, root.data, max_range)

    return isLeftWithinConstraint and isRightWithinConstraint




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



root = takeLevelWiseTreeInput()

print("Structure of Tree you entered is: ")
printLevelWise(root)
# print("\nIs it a BST ?", isBST(root))
# print("\nIs it a BST ?", isBST2(root))
print("\nIs it a BST ?", isBST3(root, -10000, 10000))