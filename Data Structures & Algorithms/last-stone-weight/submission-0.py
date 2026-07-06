class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            x = -1 * heapq.heappop(max_heap)
            y = -1 * heapq.heappop(max_heap)
            if x != y:
                diff = max(x,y) - min(x,y)
                heapq.heappush(max_heap, -1 * diff)
        
        return -1 * max_heap[0] if max_heap else 0
