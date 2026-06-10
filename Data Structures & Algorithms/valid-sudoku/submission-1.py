class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_rows = collections.defaultdict(set)
        dict_cols = collections.defaultdict(set)
        dict_sqs = collections.defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in dict_rows[r] or 
                    board[r][c] in dict_cols[c] or
                    board[r][c] in dict_sqs[(r//3, c//3)]
                ):
                    return False
                dict_rows[r].add(board[r][c])
                dict_cols[c].add(board[r][c])
                dict_sqs[(r//3, c //3)].add(board[r][c])
        return True
