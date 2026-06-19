class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l = 1
        r = max_pile
        ans = max_pile + 1

        while l<=r:
            k = (l+r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/ k)
            if hours > h:
                l = k + 1
            else:
                ans = min(ans, k)
                r = k - 1
        
        return ans