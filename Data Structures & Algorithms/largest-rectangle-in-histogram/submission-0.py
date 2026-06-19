class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            new_index = i
            while stack and heights[i] < stack[-1][1]:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(max_area, area)
                new_index = index

            stack.append((new_index,heights[i]))
        
        while stack:
            index, height = stack.pop()
            area = height * (len(heights) - index)
            max_area = max(max_area, area)
        
        return max_area

                