# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cache = {}
        def dfs(n, low, high):
            if n is None: 
                return True
            if n in cache:
                return cache[n]
            if n.left == None and n.right == None:
                return low < n.val < high
            elif n.left == None and n.right != None:
                return n.val < n.right.val and dfs(n.right, n.val, high)
            elif n.left != None and n.right == None:
                return n.val > n.left.val and dfs(n.left, low, n.val)
            else:
                res = n.left.val < n.val < n.right.val and dfs(n.left, low, n.val) and dfs(n.right, n.val, high)
                cache[n] = res
                return res
        return dfs(root, -float("inf"), float("inf"))