class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)
        
        for c in range(9):
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if(board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in sqrs[r // 3, c // 3]
                  ):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sqrs[r // 3, c // 3].add(board[r][c])
        return True