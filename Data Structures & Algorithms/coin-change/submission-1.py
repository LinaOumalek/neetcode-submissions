class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(curr, memo):
            if curr in memo:
                return memo[curr]
            if curr == amount:
                return 0
            if curr > amount:
                return float("inf")
            
            res = []
            for i in range(len(coins)):
                res.append(dfs(curr + coins[i], memo)) 
            memo[curr] = 1 + min(res)
            return memo[curr]

        res = dfs(0, dict())
        if res == float("inf"):
            return -1
        return res