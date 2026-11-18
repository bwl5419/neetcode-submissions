class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = set()
        path = []
        def dfs():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for num in nums:
                if num in used:
                    continue
                path.append(num)
                used.add(num)
                dfs()
                path.pop()
                used.remove(num)
        dfs()
        return result
        