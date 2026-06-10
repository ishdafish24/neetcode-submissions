class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_rows = collections.defaultdict(list)
        dict_cols = collections.defaultdict(list)
        dict_sqs = collections.defaultdict(list)
        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in dict_rows[r] or 
                    board[r][c] in dict_cols[c] or
                    board[r][c] in dict_sqs[(r//3, c//3)]
                ):
                    return False
                dict_rows[r].append(board[r][c])
                dict_cols[c].append(board[r][c])
                dict_sqs[(r//3, c //3)].append(board[r][c])
        return True
