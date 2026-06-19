class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = {}
        for c in s1:
            freq1[c] = freq1.get(c,0) + 1
        freq2 = {}
        
        l = 0
        for r in range(len(s2)):
            freq2[s2[r]] = freq2.get(s2[r],0) + 1
            if r-l+1 == len(s1):
                if freq1 == freq2:
                    return True
                freq2[s2[l]] -= 1
                if freq2[s2[l]] == 0:
                    del freq2[s2[l]]
                l += 1

        return False
            

            