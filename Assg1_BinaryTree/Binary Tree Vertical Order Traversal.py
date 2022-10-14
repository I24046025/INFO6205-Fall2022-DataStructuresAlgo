# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: 
            return []

        tempDict = collections.defaultdict(list)
        queue = collections.deque([(0, root)])
        res = []
        maxX, minX = 0, 0

        while queue:
            x, curr = queue.popleft()
            tempDict[x].append(curr.val)

            # record the max and min of the x-axis
            minX = min(minX, x)
            maxX = max(maxX, x)

            if curr.left:
                queue.append((x-1, curr.left))
            if curr.right:
                queue.append((x+1, curr.right))
            
        for i in range(minX, maxX+1):
            res.append(tempDict[i])
        return res