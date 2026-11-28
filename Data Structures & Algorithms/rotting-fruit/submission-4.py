from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        cfresh = 0

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    cfresh += 1
                if grid[i][j] == 2:
                    q.append((i,j))

        mn =0
        while q and cfresh >0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for ni, nj in directions:
                    if (0<= ni +i <len(grid) and 0<= nj + j <len(grid[0])) and grid[ni +i][nj + j] == 1:
                        grid[ni+i][nj+j] = 2
                        q.append((ni+i, nj+j))
                        cfresh-=1
            mn += 1

        if cfresh > 0:
            return -1
        else:
            return mn

