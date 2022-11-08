# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from  collections import deque
class Codec:

    def serialize(self, root):
        if root == None: 
            return  ''
        q = deque([(root)]) 
        l = []
        while q:
            n = q.popleft()
            if n != None:
                q.append(n.left)
                q.append(n.right)
                l.append(str(n.val))
            else:
                l.append('Null')

        return ' '.join(l)
    
    def deserialize(self, data):
        if data == '': return None
        array = data.split(' ')
        root = TreeNode(int(array[0]))
        q = deque([root])
        index = 1
        while q:
            n = q.popleft()
            if array[index] != 'Null':
                n.left = TreeNode(int(array[index]))
                q.append(n.left)
            index += 1
            if array[index] != 'Null':
                n.right = TreeNode(int(array[index]))
                q.append(n.right)
            index += 1
        return root
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans