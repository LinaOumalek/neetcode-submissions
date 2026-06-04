class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        minutes = 0
        fresh = 0
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        while fresh >0 and queue:
            l = len(queue)
            for i in range(l):
                r, c = queue.popleft()
                for nr, nc in dirs:
                    if 0<= nr + r <len(grid) and 0<= nc +c <len(grid[0]) and grid[nr+r][nc+c] == 1:
                        grid[nr+r][nc+c] = 2
                        fresh -= 1
                        queue.append((nr+r, nc+c))

            minutes += 1
        
        return minutes if fresh == 0 else -1