# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        d = deque([root])
        res = []
        while len(d) > 0:
            lvl = []
            for i in range(len(d)):
                node = d.popleft()
                lvl.append(node.val)
                if node.left is not None:
                    d.append(node.left)
                if node.right is not None:
                    d.append(node.right)
            res.append(lvl)
        return res
