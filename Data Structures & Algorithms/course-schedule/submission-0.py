class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited= set()

        def buildGraph(edges):
            res = {}
            for a,b in edges:
                if a not in res:
                    res[a] = []
                if b not in res:
                    res[b] = []
                res[b].append(a)

            return res
        def dfs(node, path):
            if node in visited:
                return True
            if node in path:
                return False

            path.add(node)

            for c in g[node]:
                if not dfs(c, path):
                    return False
           
            visited.add(node)
            return True
        g = buildGraph(prerequisites)

        for node in g:
            if node not in visited:
                if not dfs(node, path = set()):
                    return False
        return True

