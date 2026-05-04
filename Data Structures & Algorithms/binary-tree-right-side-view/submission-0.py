# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
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
                res.append(level[-1])
        
        return res