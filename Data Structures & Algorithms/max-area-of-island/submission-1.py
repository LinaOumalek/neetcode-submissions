class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        tmax = 0

        def dfs(i,j):
            if not (0<= i <len(grid) and 0<= j <len(grid[0])):
                return 0
            if grid[i][j] == 0 or (i,j) in visited:
                return 0
            visited.add((i,j))
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            res = 1
            for ni, nj in directions:
                res += dfs(ni+i, nj +j)
            return res

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    tmax = max(tmax, dfs(i,j))
        return tmax
