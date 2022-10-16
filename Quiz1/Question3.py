# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Question3(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque([root])

        while q:
            temp = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    temp.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if temp:
                res.append(temp)
        return res