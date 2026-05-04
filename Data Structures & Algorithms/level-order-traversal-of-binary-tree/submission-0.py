# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[root.val]]
        queue = deque([root])

        while queue:
            level = []
            level_size = len(queue)
            for _ in range(level_size):
                current_node = queue.popleft()
                if current_node.left:
                    level.append(current_node.left.val)
                    queue.append(current_node.left)
                if current_node.right:
                    level.append(current_node.right.val)
                    queue.append(current_node.right)
            if level:
                res.append(level)
        
        return res


