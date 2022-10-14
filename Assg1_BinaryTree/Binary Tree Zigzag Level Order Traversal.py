# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q = collections.deque([root])
        res = []
        level = 0
        
        while q:
            temp = collections.deque()

            for i in range(len(q)):
                curr = q.popleft()
                if level % 2 == 0:
                    temp.append(curr.val)
                else:
                    temp.appendleft(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(temp)
            level += 1
        return res