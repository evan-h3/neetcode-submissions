class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        #loop to first height > 0
        while height[l] == 0:
            l+=1
        r = l+1

        max_area = 0
        while l<r and r<len(height):
            if height[r] >= height[l]:
                length = r-l-1
                width = min(height[l], height[r]) 
                max_area += (length * width) - sum(height[l+1:r])
                l = r
            r += 1

        return max_area

        #algo: 
        # move r until height[r] >= height[l]
        # calc the area and add it
        # subtract sum of heights in between to avoid overcounting
