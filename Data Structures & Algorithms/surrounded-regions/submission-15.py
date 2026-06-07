class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows = len(board)
        cols = len(board[0])
        dirs = [(1,0), (0,1), (-1,0),(0,-1)]

        def dfs(r,c,region):
            if not (0<= r<rows and 0<= c<cols):
                return False
            if board[r][c] == "X":
                return True
            
                
            visited.add((r,c))
            region.append((r,c))
            res = True
            for nr, nc in dirs:
                if (nr+r, nc+c) not in visited:
                    if not dfs(nr+r, nc+c, region):
                        res = False
            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    region = []
                    res = dfs(r, c, region)
                    if res == True:
                        for x, y in region:
                            board[x][y] = "X"
        
        

