class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2

        def dfs(start, target, memo):
            if target in memo:
                return memo[target]
            if target < 0:
                return False 
            if target == 0:
                return True
            
            for i in range(start, len(nums)):
                if dfs(i+1, target - nums[i], memo):
                    return True
            return False
        return dfs(0, target, {})
