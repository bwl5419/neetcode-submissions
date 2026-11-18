class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        def dfs(i, total):
            if total == target:
                result.append(path[:])
                return
            if total > target or i == len(candidates):
                return 
            path.append(candidates[i])
            dfs(i+1,total+ candidates[i])
            path.pop()
            
            while i + 1 < len(candidates) and candidates[i+1] ==candidates[i]:
                i+=1
            dfs(i+1,total)
        candidates.sort()
        dfs (0,0)
        return result
