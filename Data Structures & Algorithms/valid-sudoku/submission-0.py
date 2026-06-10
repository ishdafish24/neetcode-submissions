class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        length = len(board)
        dict_rows = collections.defaultdict(list)
        dict_cols = collections.defaultdict(list)
        dict_boxes = collections.defaultdict(list)
        for r in range(length):
            for c in range(length):
                if board[r][c] != ".":
                    dict_rows[r].append(board[r][c])
                    dict_cols[c].append(board[r][c])
                    dict_boxes[(r // 3, c // 3)].append(board[r][c])
        for i in range(length):
            if (len(set(dict_rows[i])) != len(dict_rows[i]) or 
                len(set(dict_cols[i])) != len(dict_cols[i])):
                    return False
        for box_vals in dict_boxes.values():
            if len(set(box_vals)) != len(box_vals):
                return False
        return True