class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # the approach is a hash of hashes
        n = len(board[0])
        rows = {i : {} for i in range(n)}
        cols = {i : {} for i in range(n)}
        square = {i : {} for i in range(n)}
        for i in range(len(board)):
            for j in range(len(board[i])):
                sq = (i // 3) * 3 + (j // 3)
                if board[i][j] == ".":
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in square[sq]:
                    return False
                rows[i][board[i][j]] = 1
                cols[j][board[i][j]] = 1
                square[sq][board[i][j]] = 1
        return True