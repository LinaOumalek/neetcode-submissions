# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max1 = 0
        def dfs(node):
            nonlocal max1
            if not node:
                return 0
            a = dfs(node.left) 
            b = dfs(node.right)
            if a + b >  max1:
                max1 = a + b
            return max(a, b) + 1
        dfs(root)
        return max1