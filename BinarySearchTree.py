#Class for a simple bianry search tree

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

#Function to insert into tree

def insert(root, node):
    if not root:
        #If there is no tree, start one
        root = node
    else:
        if root.val < node.val:
            #If node to be inserted is greater than root,
            #Look at the right of the BST
            if not root.right:
                #If theres nothing there, insert the node
                root.right = node
            else:
                #Or recursively check the tree, now starting at right node
                insert(root.right, node)
        else:
            if not root.left:
                root.left = node
            else:
                insert(root.left, node)

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val))
        inorder(root.right)

    
#TESTS
n0 = Node(11)                    
n1 = Node(10)
n2 = Node(15)
n3 = Node(20)
n4 = Node(0)
n5 = Node(-5)

insert(n0, n1)
insert(n0, n2)
insert(n0, n3)
insert(n0, n4)
insert(n0, n5)

inorder(n0)


