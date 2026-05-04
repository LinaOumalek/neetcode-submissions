# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 1

        def dfs(root):
            if not root:
                return
            
            if root.left:
                if root.left.val < root.val:
                    root.left.val = root.val
                else:
                    self.count += 1
                dfs(root.left)
            
            if root.right:
                if root.right.val < root.val:
                    root.right.val = root.val
                else:
                    self.count += 1
                dfs(root.right)
        dfs(root)
        return self.count
            

            