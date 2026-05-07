class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(s):
            l,r = 0,len(s)-1
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    res += 1
        return res