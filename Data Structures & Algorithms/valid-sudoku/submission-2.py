class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        section = defaultdict(set)
        N = len(board)
        M = len(board[0])
        #loop through and store value in each row/column/section
        for i in range(N):
            for j in range(N):
                #check validity
                if board[i][j] in rows[i] or board[i][j] in cols[i] or board[i][j] in [(i//3,j//3)]:
                    return False
                #append for each case
                rows[i].add(board[i][j])
                cols[i].add(board[i][j])
                section[(i//3,j//3)].add(board[i][j])

        return True
        