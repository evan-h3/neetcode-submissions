class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        #loop through nums and only do check if curr is > 0
        for i in range(len(nums)):
            #if curr is > 0 then it's impossible to find somethign that sums to 0
            if nums[i] > 0:
                break
            #skip possible duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            #use two pointers to find numbers that add up with curr to = 0
            l, r = i+1, len(nums)-1
            while l<r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum > 0:
                    r-=1
                elif curr_sum < 0:
                    l+=1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                    
        return ans

            
        


        