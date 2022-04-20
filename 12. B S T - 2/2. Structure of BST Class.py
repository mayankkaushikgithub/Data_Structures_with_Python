
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.numNodes = 0

    # ------------------------- PRINTING FUNCTIONS -----------------
    def printTreeHelper(self, root):
        if root == None:                                # Base Case root == none means tree is emtpy
            return
        print(root.data, end=" : ")
        if root.left != None:                           # if no left node is there it won't execute
            print("L:", root.left.data, end=" , ")
        if root.right != None:                          # if no right node is there it won't execute
            print("R:", root.right.data, end="")
        print()
        self.printTreeHelper(root.left)                 # recursively call function
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)
    #-------------------------------------------------------------------


    #--------------------------- SEARCHING FUNCTIONS ----------------
    def isPresentHelper(self, root, data):              # helper function of isPresent()
        if root == None:
            return False
        if root.data == data:
            return True
        if root.data < data:
            return self.isPresentHelper(root.right, data)
        else:
            return self.isPresentHelper(root.left, data)

    def search(self, data):         # Time Complexity: O(height) & Worst: O(n)
        return self.isPresentHelper(self.root, data)
    # ------------------------------------------------------------------------


    #-------------------------- INSERTION FUNCTIONS ---------------------
    def insertHelper(self, root, data):
        if root == None:
            node = BinaryTreeNode(data)
            return node
        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root
        else: # root.data <= data:
            root.right = self.insertHelper(root.right, data)
            return root

    def insert(self, data):             # Time Complexity: O(height) & Worst: O(n)
        self.numNodes += 1 # for total no. of nodes
        self.root = self.insertHelper(self.root, data)
    # ------------------------------------------------------------------------


    #---------------------------- DELETE FUNCTIONS--------------------------

    def min(self, root):                           # to find minimum of right sub tree
        if root == None:
            return 10000
        if root.left == None:
            return root.data
        return self.min(root.left)

    def deleteDataHelper(self, root, data):
        if root == None:
            return False, None

        if root.data < data:
            deleted, newRightNode = self.deleteDataHelper(root.right, data)
            root.right = newRightNode
            return deleted, root

        if root.data > data:
            deleted, newLeftNode = self.deleteDataHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root

        # if root.data == data:
        if root.left == None and root.right == None:        # for leaf node to be deleted
            return True, None
        if root.left == None:                               # root has only right child
            return True, root.right
        if root.right== None:                               # root has only left child
            return True, root.left

        replacement = self.min(root.right)
        root.data = replacement
        deleted, newRightNode = self.deleteDataHelper(root.right, replacement)
        root.right = newRightNode
        return True, root

    def delete(self, data):                                  # Time Complexity: O(height) & Worst: O(n)
        deleted, newRoot = self.deleteDataHelper(self.root, data)
        if deleted:
            self.numNodes -= 1
        self.root = newRoot
        return deleted

    # ------------------------------------------------------------------------

    def count(self):
        return self.numNodes



b = BST()
print("Enter Total Number of Test Cases you want to perfom: ")
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
    # if choice == 4:
        b.printTree()

'''
INPUT 1:
6
1 2
1 3
1 1
4
2 2
4

INPUT 2:
8
1 4
1 4
1 4
1 4
4
3 4
2 4
4

INPUT 3:
6
1 2
1 3
1 1
3 2
2 2
3 2
'''