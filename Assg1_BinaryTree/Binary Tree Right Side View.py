# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
    def rightSideView(self, root):
        res = []
        q = collections.deque([root])
        
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    if i == 0:
                        res.append(curr.val)
                    if curr.right:
                        q.append(curr.right)
                    if curr.left:
                        q.append(curr.left)
        return res