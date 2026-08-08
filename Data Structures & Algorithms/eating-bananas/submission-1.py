class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)
        valid = []

        for rate in range(1,maximum+1):
            curr = 0
            for p in piles:
                curr += math.ceil(p/rate)
            if curr <= h:
                valid.append(rate)

        return min(valid)
