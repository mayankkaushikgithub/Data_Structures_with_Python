class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def numLeafNodes(root):                                         # METHOD TO FIND NO. OF LEAF NODES

    if root == None:                                            # Base Case - 1
        return 0

    if root.left is None and root.right is None:                # Base Case - 2
        return 1

    leftNumLeaf = numLeafNodes(root.left)
    rightNumLeaf = numLeafNodes(root.right)

    return leftNumLeaf + rightNumLeaf





#------------------------------ Input/Output Functions

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

root = treeInput()
printTreeDetailed(root)
print(numLeafNodes(root))