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




#---------------------------- METHOD - 1 -------------------------------#
# Time Complexity: O(n^2)
#
# def height(root):
#     if root == None:
#         return
#     return 1 + max(height(root.left), height(root.right))
#
# def isBalanced(root):
#
#     if root == None:                                        # Base Case
#         return
#
#     lh = height(root.left)                              # find height of both sides individually
#     rh = height(root.right)
#
#     if lh - rh > 1 or rh - lh > 1:
#         return False
#
#     isLeftBalanced =isBalanced(root.left)
#     isRightBalanced =isBalanced(root.right)
#
#     if isLeftBalanced and isRightBalanced:
#         return True
#     else:
#         return False

#-----------------------------------------------------------------------------#

#-------------------------------METHOD - 2 (Better)-----------------------------#
# Time Complexity: O(n)

def getHeightAndCheckBalanced(root):

    if root == None:
        return 0, True

    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)

    h = 1 + max(lh, rh)

    if lh - rh > 1 or rh - lh > 1:
        return h, False

    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False

#----------------------------------------------------------------------------#
def isBalanced2(root):
    h, isRootBalanced = getHeightAndCheckBalanced(root)
    return isRootBalanced           # now fun. will only return only 1 value




root = treeInput()
printTreeDetailed(root)
print()
# print(isBalanced(root))
print(getHeightAndCheckBalanced(root))