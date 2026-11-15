class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0 
        start= 0 
        end = len(heights) -1
        while end > start:
            width = end - start
            height = min(heights[start],heights[end])
            maxarea= max(maxarea, width*height)
            if heights[start] > heights[end]:
                end -=1
            else:
                start +=1
        return maxarea