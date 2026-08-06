class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i,len(heights)):
                min_height = min(min_height, heights[j])
                curr_area = min_height * (j-i+1)
                max_area = max(max_area, curr_area)
        return max_area
