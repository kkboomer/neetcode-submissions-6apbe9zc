# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        traverse = []
        if root is not None:
            traverse.extend([root.val])
        traverse.extend(self.preorderTraversal(root.left))
        traverse.extend(self.preorderTraversal(root.right))
        return traverse