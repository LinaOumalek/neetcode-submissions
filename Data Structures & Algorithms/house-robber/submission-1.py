class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def dfs(i, memo):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0
            memo[i] = nums[i] + max(dfs(i+2, memo), dfs(i+3, memo))
            return memo[i]
        
        return max(dfs(0, dict()), dfs(1, dict()))