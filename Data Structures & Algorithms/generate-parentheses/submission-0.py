class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def dfs(curr, n, opn, close):
            if len(curr) == n*2:
                self.res.append("".join(curr[:]))
                return
            
            if opn < n:
                curr.append('(')
                dfs(curr, n, opn+1, close)
                curr.pop()
            
            if opn > close:
                curr.append(')')
                dfs(curr, n, opn, close + 1)
                curr.pop()
        dfs([], n, 0, 0)
        return self.res