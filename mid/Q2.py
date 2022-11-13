class Node:
   
    def __init__(self, val):
       
        self.val = val
        self.left = None
        self.right = None
 
def findParent(node, value, parent):
    # base case
    if node is None:
        return
 
    if (node.val == value):
        # if it is the top root of the binary tree
        if (parent == -1):
            print(node.val)
        else:
            print(parent)
    else:
        findParent(node.left, value, node.val)
        findParent(node.right, value, node.val)
 

# test
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.left = Node(7)
targetNode = 1
# run
findParent(root, targetNode, -1)
