class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows,cols = [], []
        boxes = {}
        for i in range(9):
            cols.append([])
            rows.append([])
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                b = (r//3,c//3)
                if b not in boxes:
                    boxes[b] = []
                if val in rows[r] or val in cols[c] or val in boxes[b]:
                    return False
                rows[r].append(val)
                cols[c].append(val)
                boxes[b].append(val)
        return True 
