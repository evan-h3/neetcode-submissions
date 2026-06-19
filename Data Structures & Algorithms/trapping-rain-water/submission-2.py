class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 1:
            return 0
        l,r = 0 , len(height)-1
        maxL = 0
        maxR = 0
        area = 0
        while l<r:
            if height[l] <= height[r]:
                if maxL > height[l]:
                    area += maxL - height[l]
                maxL = max(maxL,height[l])
                l+=1
            else:
                if maxR > height[r]:
                    area += maxR - height[r]
                maxR = max(maxR,height[r])
                r-=1
        return area


            
