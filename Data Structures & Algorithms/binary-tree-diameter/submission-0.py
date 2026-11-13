# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_depth = 0 
        def dfs(node):
            nonlocal max_depth
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            d = l+r
            max_depth = max(max_depth, d)
            return max(l, r) + 1
        dfs(root)
        return max_depth