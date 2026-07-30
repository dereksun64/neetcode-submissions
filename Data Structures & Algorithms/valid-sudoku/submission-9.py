class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squs = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] in rows[r] or board[r][c] in cols[r] or board[r][c] in squs[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squs[(r//3, c//3)].add(board[r][c])
        return True