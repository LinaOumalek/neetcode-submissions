class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def dfs(target, curr, start):
            if target < 0:
                return
            if target == 0:
                self.res.append(curr[:])
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs( target - nums[i], curr, i)
                curr.pop()
        dfs(target, [], 0)
        return self.res