class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(nums, current):
            if nums == []:
                self.res.append(current[:])
                return
            
            for i in range(len(nums)):
                current.append(nums[i])
                dfs(nums[:i] + nums[i+1:], current)
                current.pop()

            
        dfs(nums, [])
        return self.res