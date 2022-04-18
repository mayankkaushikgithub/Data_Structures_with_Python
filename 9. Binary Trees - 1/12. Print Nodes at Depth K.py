class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetailed(root):                                 # METHOD to print the tree
    if root == None:                                         # Base Case root == none means tree is emtpy
        return
    print(root.data, end=" : ")
    if root.left != None:                                   # if no left node is there it won't execute
        print("L", root.left.data, end=" , ")
    if root.right != None:                                  # if no right node is there it won't execute
        print("R", root.right.data, end="")
    print()
    printTreeDetailed(root.left)                            # recursively call function
    printTreeDetailed(root.right)

def treeInput():                                             # METHOD to take input
    rootData = int(input())                                     # take i/p of nodes
    if rootData == -1:                                          # BASE CASE
        return
    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root





# def printDepthK(root, k):                                           # METHOD - 1
#     if root == None:
#         return
#     if k == 0:
#         print(root.data)
#         return
#     printDepthK(root.left, k-1)
#     printDepthK(root.right, k-1)

def printDepthK(root, k, d=0):                                           # METHOD - 1
    if root == None:                                                # Base Case 1
        return

    if k == d:                                                      # Base Case 2 when root is found
        print(root.data)
        return

    printDepthK(root.left, k, d+1)                                  # go downwards left
    printDepthK(root.right, k, d+1)                                 # go downwards right



root = treeInput()
printTreeDetailed(root)
