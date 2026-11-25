class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        nums = sorted(candidates)

        def dfs(target, curr, start):
            if target < 0:
                return
            if target == 0:
                self.res.append(curr[:])
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                dfs( target - nums[i], curr, i+1)
                curr.pop()
        dfs(target, [], 0)
        return self.res