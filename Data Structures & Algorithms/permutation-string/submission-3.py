class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        freq1 = [0] * 26
        freq2 = [0] * 26
        l = 0
        
        #populate freq1 with letters in s1
        for s in s1:
            freq1[ord(s) - ord('a')] += 1

        for r in range(len(s2)):
            freq2[ord(s2[r]) - ord('a')] += 1

            #if curr visitng str len is > then s1 shrink until valid
            if r-l+1 > len(s1):
                freq2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if freq1 == freq2:
                return True

        return False
        
                