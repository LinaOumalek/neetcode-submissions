from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))
        while queue:
            i, j = queue.popleft()

            for ni, nj in directions:
                if (0<= ni +i <len(grid) and 0<= nj + j <len(grid[0])) and grid[ni +i][nj + j] ==2147483647:
                    grid[ni+i][nj+j] = grid[i][j] + 1

                    queue.append((ni+i, nj+j))

