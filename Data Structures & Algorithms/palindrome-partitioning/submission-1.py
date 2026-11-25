class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(s):
            return s == s[::-1]
        
        def dfs(s, curr):
            if len(s) ==0:
                self.res.append(curr[:])
                return
            
            for i in range(len(s)):
                subs = s[:i+1]
                if palindrome(subs):
                    curr.append(subs)
                    dfs(s[i+1:], curr)
                    curr.pop()
        self.res = []
        dfs(s, [])
        return self.res
