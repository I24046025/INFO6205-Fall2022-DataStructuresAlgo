# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or root == p or root == q:
            return root

        # Find p/q in left subtree
        l = self.lowestCommonAncestor(root.left, p, q)
		
		# Find p/q in right subtree
        r = self.lowestCommonAncestor(root.right, p, q)
        
        if l and r:
            return root

        return l if l else r