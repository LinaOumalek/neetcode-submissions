class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def dfs(i, memo):
            if i in memo:
                return memo[i]
            if i == len(cost)-1 or i == len(cost) - 2:
                return cost[i]
            memo[i] = cost[i] + min(dfs(i+1, memo), dfs(i+2, memo))
            return memo[i]
        
        return min(dfs(0, dict()), dfs(1, dict()))