class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        rate = max(piles)
        while l<r:
            mid = (l+r) // 2

            curr = 0
            for p in piles:
                curr += math.ceil(p/mid)
            if curr > h:
                l = mid + 1
            else:
                r = mid - 1
                rate = min(rate, mid)
            
        return rate
