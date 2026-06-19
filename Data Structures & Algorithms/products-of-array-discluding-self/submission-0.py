class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [None] * len(nums)
        prefix[0] = nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i]

        suffix = [None] * len(nums)
        suffix[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        output = [None] * len(nums)
        output[0] = suffix[1]
        output[-1] = prefix[-2]
        for i in range(1,len(nums)-1):
            output[i] = prefix[i-1] * suffix[i+1]
        
        return output



            