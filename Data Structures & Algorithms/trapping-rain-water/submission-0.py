class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        l,r = 0 , 1
        width = 0
        block = 0
        area = 0
        while r < len(height):
            if height[r] < height[l]:
                width+=1
                block+=height[r]
                r+=1
            else:
                area += (height[l] * width) - block
                width = 0
                block = 0
                l = r
                r+=1
        return area


            
