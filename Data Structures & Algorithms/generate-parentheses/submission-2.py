class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def dfs(curr, o, c):
            if o+c == 2*n:
                self.res.append("".join(curr))
                
            
            if o < n:
                curr.append("(")
                dfs(curr, o+1,c)
                curr.pop()
            if o > c:
                curr.append(")")
                dfs(curr, o,c+1)
                curr.pop()
        dfs([], 0, 0)
        return self.res
