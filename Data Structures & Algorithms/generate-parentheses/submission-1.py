class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        def dfs(open_count, closed_count):
            if open_count == closed_count == n:
                result.append("".join(path))
                return
            if open_count < n:
                path.append("(")
                dfs(open_count +1, closed_count)
                path.pop()
            if closed_count < open_count:
                path.append(")")
                dfs(open_count, closed_count+1)
                path.pop()
        dfs(0,0)
        return result
            