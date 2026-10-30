# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if node is None:
                return None
            if node.val == p.val or node.val == q.val:
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            if l is not None and r is not None:
                return node
            if (l is not None and r is None):
                return l
            else:
                return r
        return dfs(root)