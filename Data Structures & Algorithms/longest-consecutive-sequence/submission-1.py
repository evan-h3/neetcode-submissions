class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #turn nums in to a set for quick lookup
        lookup = set(nums)
        max_length = 0

        #loop through nums to check if number is a starting number
        for i in range(len(nums)):
            #if not starting
            if nums[i]-1 in lookup:
                continue
            #if it is then go find the next consec num present in list
            # and track the curr length 
            length = 0
            curr = nums[i]
            while curr in lookup:
                length+=1
                curr+=1
            max_length = max(max_length, length)
    
        return max_length
        #return the longest consecutive length

