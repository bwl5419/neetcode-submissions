class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        def dfs(i):
            if i == len(s):
                result.append(path[:])
                return 
            for j in range(i, len(s)):
                piece = s[i:j+1]
                if piece != piece[::-1]:
                    continue
                path.append(piece)
                dfs(j+1)
                path.pop()
        dfs(0)
        return result