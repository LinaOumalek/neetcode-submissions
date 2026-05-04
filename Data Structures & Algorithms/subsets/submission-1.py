class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(nums, current, i):
            if i == len(nums):
                self.res.append(current[:])
                return
            
            dfs(nums, current, i+1)
            current.append(nums[i])
            dfs(nums, current, i+1)
            current.pop()
        
        dfs(nums, [], 0)
        return self.res
