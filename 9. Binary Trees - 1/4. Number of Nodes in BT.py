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

def treeInput():                                                # METHOD to take i/p

    rootData = int(input())                                     # take i/p of nodes
    if rootData == -1:                                          # BASE CASE
        return

    root = BinaryTreeNode(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root




def numNodes(root):                                             # METHOD TO COUNT NUMBER OF NODES
    if root == None:
        return 0
    leftCount = numNodes(root.left)
    rightCount = numNodes(root.right)
    return 1 + leftCount + rightCount

root = treeInput()
printTreeDetailed(root)