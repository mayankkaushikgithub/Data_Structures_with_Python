class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# def printTree(root):                                        # METHOD - 1 (not good)
#     if root == None:
#         return
#     print(root.data)
#     printTree(root.left)
#     printTree(root.right)

def printTreeDetailed(root):                                 # METHOD - 2
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



btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)

btn4 = BinaryTreeNode(4)
btn5 = BinaryTreeNode(5)

btn1.left = btn2
btn1.right = btn3
btn2.left = btn4
btn2.right = btn5


printTreeDetailed(btn1)




