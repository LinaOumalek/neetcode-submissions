class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c>=len(grid[0]) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            directions = [(1, 0), (0, 1), (-1,0), (0,-1)]
            res = 1
            for nr, nc in directions:
                res += dfs(r + nr, c +nc)
            return res

        max_counter = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = dfs(r,c)
                    max_counter = max(max_counter, res)
        return max_counter