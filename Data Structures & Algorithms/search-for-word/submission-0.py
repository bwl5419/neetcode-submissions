class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, cols = len (board), len(board[0])
        paths = set()
        def dfs(r,c,k):
            if k == len(word):
                return True
            if (r<0 or c < 0 or r>= row or c >= cols) or board[r][c] != word[k] or (r,c) in paths:
                return False
            paths.add((r,c))
            found = (dfs(r+1, c, k+1)) or dfs(r-1,c, k+1) or dfs(r,c+1,k+1) or dfs(r,c-1,k+1)
            paths.remove((r,c))
            return found
        for r in range(row):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False
