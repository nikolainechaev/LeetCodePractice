class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        sqrs = defaultdict(set)

        for c in range(9):
            for r in range(9):
                if board[r][c] == '.':
                    continue
                if (
                    board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                    board[r][c] in sqrs[r // 3, c // 3]
                ):
                    return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                sqrs[r//3, c//3].add(board[r][c])
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         cols = defaultdict(set)
#         rows = defaultdict(set)
#         sqrs = defaultdict(set)
        
#         for r in range(9):
#             for c in range(9):
#                 if board[r][c] == '.':
#                     continue
#                 if(
#                     board[r][c] in cols[c] or #forgot about index for cols -> "cols[c]"
#                     board[r][c] in rows[r] or #forgot about index for rows -> "rows[r]"
#                     board[r][c] in sqrs[r//3, c//3] #forgot about "[r//3, c//3]"
#                 ):
#                     return False
#                 cols[c].add(board[r][c]) #forgot that i should add number to specific [c]
#                 rows[r].add(board[r][c]) #forgot that i should add number to specific [r]
#                 sqrs[r//3, c//3].add(board[r][c]) #forgot that i should add number to specific [r//3, c//3]
#         return True