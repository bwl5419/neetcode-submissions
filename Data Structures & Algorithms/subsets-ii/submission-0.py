class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        path =[]
        nums.sort()
        def dfs(i):
            if i ==len(nums):
                result.append(path[:])
                return
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            while i +1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            dfs(i+1)
        dfs(0)
        return result

