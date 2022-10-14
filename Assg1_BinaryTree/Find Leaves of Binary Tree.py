# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def postOrder(root):
            
            if not root:
                return 0

            leftLevel = postOrder(root.left)
            rightLevel = postOrder(root.right)
            currLevel = max(leftLevel, rightLevel) + 1

            dic[currLevel].append(root.val)
            return currLevel

        dic, res = collections.defaultdict(list), []
        postOrder(root)

        for i in range(1, len(dic) + 1):
            res.append(dic[i])
        return res