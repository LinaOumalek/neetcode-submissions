class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(row,col):
            distance=0
            queue = deque([(row,col, 0)])
            directions = [(1, 0), (0, 1), (-1,0), (0,-1)]

            while queue:
                r, c, distance = queue.popleft()
                if distance > grid[r][c]:
                    continue
                grid[r][c] = distance

                for nr, nc in directions:
                    if 0<=nr +r <len(grid) and 0<=nc +c<len(grid[0]) and grid[nr+r][nc+c] != 0 and grid[nr+r][nc+c] != -1:
                        queue.append((nr+r,nc+c, distance +1))
            return
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    bfs(r,c)