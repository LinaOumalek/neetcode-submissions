class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(target, memo):
            if target in memo:
                return memo[target]
            if target < 0:
                return False
            if target == 0:
                return 0
            cmin= []
            for i in range(len(coins)):
                r = dfs(target - coins[i], memo)
                if r is not False:
                    cmin.append(r)
            if cmin:
                memo[target] = 1 + min(cmin)
                return memo[target]
            else:
                memo[target] = False
                return memo[target]
        res = dfs(amount, {})
        if  res is False:
            return -1
        return res
