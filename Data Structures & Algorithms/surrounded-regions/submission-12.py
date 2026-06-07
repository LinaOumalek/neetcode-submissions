class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = set()
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, region):
            if not (0 <= r < rows and 0 <= c < cols):
                return False

            if board[r][c] == "X":
                return True



            visited.add((r, c))
            region.append((r, c))

            surrounded = True

            for dr, dc in dirs:
                if (r+dr,c+dc) not in visited:
                    if not dfs(r + dr, c + dc, region):
                        surrounded = False

            return surrounded

        for r in range(rows):

            for c in range(cols):

                if board[r][c] == "O" and (r, c) not in visited:

                    region = []

                    res = dfs(r, c, region)

                    if res == True:

                        for x, y in region:

                            board[x][y] = "X" 
        
        

