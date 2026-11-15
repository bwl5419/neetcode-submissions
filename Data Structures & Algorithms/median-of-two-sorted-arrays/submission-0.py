class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comb= []
        for item in nums1:
            comb.append(item)
        for item in nums2:
            comb.append(item)
        comb.sort()
        if len(comb) %2 ==1:
            return comb[len(comb)//2]
        else:
            return 0.5* ((comb[len(comb)//2] + comb[(len(comb)//2)-1]))
        