class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(nums, i, curr):
            if i == len(nums):
                self.res.append(curr[:])
                return
            
            dfs(nums, i+1, curr)
            curr.append(nums[i])
            dfs(nums, i+1, curr)
            curr.remove(nums[i])
        dfs(nums, 0, [])
        return self.res