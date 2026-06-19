class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = M = len(board)
        
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        BOX = defaultdict(set)

        for i in range(N):
            for j in range(i,M):
                val = board[i][j]
                if val == '.':
                    continue
                if val in ROWS[i] or val in COLS[j] or val in BOX[(i//3,j//3)]:
                    return False
                ROWS[i].add(val)
                COLS[j].add(val)
                BOX[(i//3,j//3)].add(val)
        
        return True
        