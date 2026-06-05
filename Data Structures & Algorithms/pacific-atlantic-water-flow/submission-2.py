class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])
        dirs = [(1,0), (0,1),(-1,0),(0,-1)]
    

        def dfs(r,c, visited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            for nr,nc in dirs:
                if 0<= nr+r<len(heights) and 0<= nc+c<len(heights[0]) and heights[nr+r][nc+c] >= heights[r][c]:
                    dfs(nr+r,nc+c,visited)

        for i in range(cols):
            dfs(0,i, pacific)
            dfs(rows-1, i, atlantic)
        
        for i in range(rows):
            dfs(i, 0, pacific)
            dfs(i, cols-1, atlantic)
        
        return list(pacific.intersection(atlantic))
        

        
            
