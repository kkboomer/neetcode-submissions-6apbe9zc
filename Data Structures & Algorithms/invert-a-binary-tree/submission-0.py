# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        d = deque([root])
        while d:
            # pop the node, add the pointers to the queue, then invert
            for i in range(len(d)):
                node = d.popleft()
                if node.left is not None:
                    d.append(node.left)
                if node.right is not None:
                    d.append(node.right)
                node.left, node.right = node.right, node.left
        return root
