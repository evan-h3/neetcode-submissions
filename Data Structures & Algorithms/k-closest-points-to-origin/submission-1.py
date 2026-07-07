class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            curr = self.calc_distance(x, y, 0, 0)
            if len(min_heap) >= k:
                shortest = min_heap[0][0]
                if curr < -shortest:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap,(-curr, x, y))
            else:
                heapq.heappush(min_heap,(-curr, x, y))

        ans = [(p[1],p[2]) for p in min_heap]

        return ans
            

    def calc_distance(self, x1, y1, x2, y2) -> int:
        return (x1 - x2)**2 + (y1 - y2)**2