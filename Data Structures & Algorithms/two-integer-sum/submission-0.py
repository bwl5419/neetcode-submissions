class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combo= {}
        for i, num in enumerate(nums):
            adder = target - num
            if adder in combo:
                return [combo[adder], i]
            else:
                combo[num] = i

        
        