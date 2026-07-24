class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l, r = 0, 0

        while r < len(nums):
            #make sure decreasing before adding
            while q and q[-1] < nums[r]:
                q.popleft()
            
            #append the curr index
            q.append(r)

            #get rid of invalid indexes not in curr window
            if l > q[0]:
                q.popleft()

            #make sure valid window before adding to res
            #since r starts at 0
            if r+1 >= k:
                res.append(nums[q[0]]) #append curr max
                l+=1
            r+=1

        return res

