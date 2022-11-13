class Node: 
  
    # Constructor to create a new node 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None


def Print(root, v1, v2): 
    
    # base case 
    if root is None: 
        return 

    if v1 < root.val: 
        Print(root.left, v1, v2) 

    if v1 <= root.val and v2 >= root.val: 
        print(root.val)

    if v2 > root.val: 
        Print(root.right, v1, v2) 

# test case
v1 = 10
v2 = 25
root = Node(20) 
root.left = Node(9) 
root.right = Node(19) 
root.left.left = Node(5) 
root.left.right = Node(12) 
  
# run
Print(root, v1, v2)
