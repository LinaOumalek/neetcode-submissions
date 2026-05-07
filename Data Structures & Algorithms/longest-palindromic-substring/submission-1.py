class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s):
            l,r = 0, len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(s, memo):
            if s in memo:
                return memo[s]
            if isPalindrome(s):
                return s
            memo[s] = max(dfs(s[1:], memo), dfs(s[:-1], memo), key = len)
            return memo[s]
        
        return dfs(s, dict())
