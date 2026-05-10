class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s, memo):
            if s in memo:
                return memo[s]
            if s == "":
                return True
            
            res = False

            for word in wordDict:
                if s[:len(word)] == word:
                    if dfs(s[len(word):], memo):
                        res = True
            memo[s] = res
            return memo[s]
        return dfs(s, dict())