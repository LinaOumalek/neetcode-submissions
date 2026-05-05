class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, nums, target, current):
            if target < 0:
                return
            if target == 0:
                self.res.append(current[:])
                return 

            for j in range(i, len(nums)):
                current.append(nums[j])
                dfs(j, nums, target-nums[j], current)
                current.pop()
        dfs(0, nums, target, [])
        return self.res