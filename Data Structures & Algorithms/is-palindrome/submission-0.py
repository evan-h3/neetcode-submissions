class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l <= r:
            while l < r and s[l].upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                l+=1
            while r > l and s[r].upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                r-=1
            
            if s[l].upper() != s[r].upper():
                return False
            l+=1
            r-=1
        return True