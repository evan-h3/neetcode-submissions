class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        max_heap = [(-nums[i], i) for i in range(k-1)]
        heapq.heapify(max_heap)

        for r in range(k-1, len(nums)):
            heapq.heappush(max_heap, (-nums[r],r))
            while max_heap[0][1] < l:
                heapq.heappop(max_heap)
            res.append(-max_heap[0][0])
            l+=1

        return res