class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.maxHeap = [n for n in nums]
        self.maxLen = k
        heapq.heapify(self.maxHeap)
        while self.maxHeap and len(self.maxHeap) > self.maxLen:
            heapq.heappop(self.maxHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxHeap, val)
        if len(self.maxHeap) > self.maxLen:
            heapq.heappop(self.maxHeap)
        return self.maxHeap[0]
        
