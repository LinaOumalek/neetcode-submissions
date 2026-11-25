class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        original = nums
        def dfs(nums, curr):
            if len(curr) == len(original):
                self.res.append(curr[:])
                return
            
            for i in range(len(nums)):
                curr.append(nums[i])
                dfs(nums[:i] + nums[i+1:], curr)
                curr.pop()
        dfs(nums, [])
        return self.res                 