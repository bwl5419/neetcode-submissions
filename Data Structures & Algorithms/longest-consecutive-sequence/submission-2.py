class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ent = set(nums)
        longest = 0 
        for num in ent:
            if num-1 in ent:
                continue
            length = 1
            while num + length in ent:
                length +=1
            longest = max(longest,length)
        return longest
      