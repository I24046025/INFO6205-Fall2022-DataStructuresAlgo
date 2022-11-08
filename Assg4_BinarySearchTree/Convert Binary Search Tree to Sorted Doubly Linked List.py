"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):

    def treeToDoublyList(self, root):
        self.prev, self.head = None, None

        if not root: return

        def inorder(curr):
            if not curr: return

            inorder(curr.left)

            if not self.prev:
                self.head = curr
            else:
                self.prev.right = curr
                curr.left = self.prev
            self.prev = curr

            inorder(curr.right)


        inorder(root)
        self.head.left = self.prev
        self.prev.right = self.head
        return self.head