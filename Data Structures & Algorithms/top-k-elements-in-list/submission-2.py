class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1

        topK = []
        for n, f in freq.items():
            heapq.heappush(topK, (f,n))
            if len(topK) > k:
                heapq.heappop(topK)
        
        return [n for f, n in topK]
                 