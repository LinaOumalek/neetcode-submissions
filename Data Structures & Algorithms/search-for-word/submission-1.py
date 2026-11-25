class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    res= self.dfs(i,j, list(word), set(), board)
                    if res == True:
                        return True
        return False
    

    def dfs(self,i, j , word, visited, board):
        if not (0<= i < len(board)) or not (0<=j< len(board[0])):
            return False
        if (i,j) in visited or board[i][j] != word[0]:
            return False
        if len(word) == 1:
            return True

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited.add((i, j))
        for ni, nj in directions:
            
            res= self.dfs(ni +i, nj+j, word[1:], visited,board)
            
            if res:
                visited.remove((i, j))
                return True
        visited.remove((i, j))
        return False
