class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(start, candidates, current, target):
            if target < 0:
                return 
            if target == 0:
                self.res.append(current[:])
                return
            
            for i in range(start, len(candidates)):
                if (i > start) and candidates[i] == candidates[i-1]:
                    continue
                current.append(candidates[i])
                dfs(i +1, candidates, current, target - candidates[i])
                current.pop()
        candidates.sort()
        dfs(0, candidates, [], target)
        return self.res