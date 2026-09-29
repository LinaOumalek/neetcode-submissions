class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        rows = len(board[0])
        cols = len(board)


        for i in range(rows):
            rows_set = set()
            for j in range(cols):
                if board[i][j] != ".":
                    if board[i][j] in rows_set:
                        return False
                    rows_set.add(board[i][j])
        
        #cols
        for i in range(cols):
            cols_set = set()
            for j in range(rows):
                if board[j][i] != ".":
                    if board[j][i] in cols_set:
                        return False
                    cols_set.add(board[j][i])
        #cubes
        coordinates = [0,3,6]
        for i in coordinates:
            for j in coordinates:
                if not helper(board, i,j):
                    return False
        return True

def helper(board,r,c):
    set2 = set()
    for i in range(r, r+3):
        for j in range(c,c+3):
            if board[i][j] != ".":
                if board[i][j] in set2:
                    return False
                set2.add(board[i][j])
    return True

