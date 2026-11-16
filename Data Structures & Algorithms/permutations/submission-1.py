class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(nums, curr):
            if len(nums) == 0:
                self.res.append(curr[:])
            
            for i in range(len(nums)):
                curr.append( nums[i])
                dfs(nums[:i] + nums[i+1:], curr)
                curr.pop()

        dfs(nums, [])
        return self.res