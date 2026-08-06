class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height)
        max_area = 0

        for i in range(len(heights)):
            start = i
            h = heights[i]
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height*(i-index))
                start = index
            stack.append((start,h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights)-i))
        
        return max_area


