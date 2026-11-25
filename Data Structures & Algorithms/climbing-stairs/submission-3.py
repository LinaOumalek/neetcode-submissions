class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(curr, memo):
            if curr in memo:
                return memo[curr]
            if curr > n:
                return 0
            if curr == n:
                return 1
            memo[curr] = dfs(curr+1, memo) + dfs(curr+2, memo)
            return memo[curr]
        return dfs(0,{})