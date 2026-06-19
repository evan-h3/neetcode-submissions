class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #create set
        #loop through array and only start checking if current num is start of a sequence
        #keep a count of consecutive sequence, and terminate when there is no consecutive element
        
        arr = set()
        for n in nums:
            arr.add(n)
        
        ans = 0

        for n in nums:
            if (n-1) not in arr: #it is start value
                count = 1
                while n+1 in arr:
                    count+=1
                    n = n+1
                ans = max(ans,count)
        
        return ans
