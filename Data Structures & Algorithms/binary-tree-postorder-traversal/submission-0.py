# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        traverse = []
        traverse.extend(self.postorderTraversal(root.left))
        traverse.extend(self.postorderTraversal(root.right))
        if root is not None:
            traverse.extend([root.val])
        return traverse