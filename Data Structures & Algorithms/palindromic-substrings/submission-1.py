class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l,r):
            c=0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-= 1
                r+= 1
                c += 1
            return c
        
        res = 0
        for i in range(len(s)):
            res += expand(i, i)
            if i + 1 < len(s):
                res += expand(i, i + 1)
        return res