class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        count = 0
        while n not in seen:
            for c in str(n):
                count += int(c)**2
            if count == 1:
                return True
            n = count
            seen.add(n)
        return False
