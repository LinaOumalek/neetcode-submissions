class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            n = len(s)
            l,r = 0, n -1
            while l<r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -=1
            return True

        self.res = []
        def dfs(current, remaining):
            if remaining == "":
                self.res.append(current[:])
                return
            
            for i in range(len(remaining)):
                if isPalindrome(remaining[:i+1]):
                    current.append(remaining[:i+1])
                    dfs(current, remaining[i+1:])
                    current.pop()
        
        dfs([], s)
        return self.res