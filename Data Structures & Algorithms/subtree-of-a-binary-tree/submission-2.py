# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not p:
                return False
            if p.val == q.val:
                a = same(p,q)
                if a:
                    return True
            return dfs(p.right, q) or dfs(p.left, q)

        def same(p,q):
            if not p and not q:
                return True
            if (p and q) and p.val == q.val:
                return same(p.right,q.right) and same(p.left,q.left)
            return False
        return dfs(root, subRoot)
