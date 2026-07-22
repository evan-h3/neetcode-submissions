class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0
        leftMax, rightMax = height[l], height[r]

        while l<r:
            if height[l] <= height[r]:
                l += 1
                #do this first to avoid adding neg, 
                #case1: if leftMax is greater then we would get the correct subtraction
                #case2: if height[l] is greater we basically just skip null out by subtracting
                #       the curr height with itself
                leftMax = max(leftMax, height[l]) 
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res
