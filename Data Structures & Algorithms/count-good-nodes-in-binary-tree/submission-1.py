# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        c = 0

        def dfs(node, curr_max):
            if not node:
                return 
            nonlocal c
            if node.val >= curr_max:
                c += 1
                curr_max = node.val
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)
        dfs(root, curr_max = float("-inf"))
        return c
