class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        
        pq = []
        for n, f in freq.items():
            heapq.heappush(pq,(f,n))
            if len(pq) > k:
                heapq.heappop(pq)
        
        ans = []
        for n in pq:
            ans.append(n[1])
        return ans