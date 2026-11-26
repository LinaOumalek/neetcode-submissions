class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(s, memo):
            if s in memo:
                return memo[s]
            if s == "":
                return True
            res = False
            for word in wordDict:
                k = len(word)
                if s[:k] == word:
                    rem = s[k:]
                    if dfs(rem, memo):
                        res = True
            memo[s] = res
            return memo[s]
        return dfs(s, {})