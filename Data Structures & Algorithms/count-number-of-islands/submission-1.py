class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        c = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(self, grid,i,j, visited)
                    c += 1
        return c

def dfs(self, grid, i, j, visited):
    if not (0 <= i < len(grid) and 0<= j <len(grid[0])):
        return
    if grid[i][j] == "0":
        return
    if (i, j) in visited:
        return
    visited.add((i,j))
    directions = [(0,1), (1,0), (-1,0),(0,-1)]
    for ni, nj in directions:
            dfs(self, grid, ni+i, nj +j, visited)