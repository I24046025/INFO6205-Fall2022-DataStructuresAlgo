# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: 
            return []

        queue = collections.deque([(root, 0)])
        width = 1

        while queue:
            for i in range(len(queue)):
                curr, idx = queue.popleft()
                if curr.left:
                    queue.append((curr.left, 2*idx))
                if curr.right:
                    queue.append((curr.right, 2*idx + 1))
            # at the same level, get the first node of value idx and the last node of value idx
            if queue:
                width = max(width, queue[-1][1]-queue[0][1]+1)
        return width