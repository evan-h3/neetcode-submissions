class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n not in seen:
            count = 0
            for c in str(n):
                count += int(c)**2
            if count == 1:
                return True
            seen.add(n)
            n = count
            
        return False
