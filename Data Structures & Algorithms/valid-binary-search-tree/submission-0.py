# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, val1, val2):
            if not root:
                return True
            
            if val1 < root.val < val2:
                return dfs(root.left, val1, root.val) and dfs(root.right, root.val, val2)
            
            return False
        
        return dfs(root, float("-inf"), float("inf"))