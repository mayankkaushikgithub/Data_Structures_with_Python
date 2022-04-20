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




import queue



def takeLevelWiseTreeInput():

    q = queue.Queue()

    print("Enter Root: ")
    rootData = int(input())                             # take the root of main/sub tree

    if rootData == -1:
        return None

    root = BinaryTreeNode(rootData)                     # make a node out of this data
    q.put(root)                                     # put this data in queue now we we'll perform on this data until -1

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
printTreeDetailed(root)
