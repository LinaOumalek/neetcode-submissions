class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited= set()
        ans = 0
        def buildGraph(edges):
            g= {}
            for a,b in edges:
                if a not in g:
                    g[a]= []
                if b not in g:
                    g[b]= []
                g[a].append(b)
                g[b].append(a)
            return g
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for c in g[node]:
                dfs(c)

        g= buildGraph(edges)
        for node in g:
            if node not in visited:
                dfs(node)
                ans += 1
        return ans + (n-len(g))
        
        