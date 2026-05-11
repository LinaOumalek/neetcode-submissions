class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        def dfs(curr, nums):
            if curr == 0:
                return True
            if curr < 0:
                return False 

            
            for i in range(len(nums)):
                num =nums[i]
                nums.remove(num)
                if dfs(curr-num, nums):
                    return True
                nums.append(num)
            return False
        return dfs(target, nums)            
            
