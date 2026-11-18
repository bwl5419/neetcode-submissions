class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        best = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r,c):
            if (r<0 or c<0 or r >= rows or c>= cols or grid[r][c]==0) or (r,c) in visited:
                return 0
            visited.add((r,c))

            return 1 + dfs(r+1,c)+ dfs(r-1,c)+ dfs(r,c+1) + dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                best = max(best, dfs(r,c))
        return best

            


        