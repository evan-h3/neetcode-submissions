class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        l = 0
        for r in range(len(nums)):
            while queue and queue[-1][0] < nums[r]:
                queue.pop()
            queue.append((nums[r],r))
            while queue and queue[0][1] < l:
                queue.popleft()
            if r-l+1 == k:
                ans.append(queue[0][0])
                l+=1

        return ans