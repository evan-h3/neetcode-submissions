class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        maximum = 0
        for i in range(len(height)):
            maximum = max(maximum,height[i])
            prefix[i] = maximum
        maximum = 0
        for i in range(len(height)-1,-1,-1):
            maximum = max(maximum,height[i])
            suffix[i] = maximum
        area = 0
        for i in range(1,len(height)-1):
            area += min(prefix[i], suffix[i]) - height[i]
        return area


            
