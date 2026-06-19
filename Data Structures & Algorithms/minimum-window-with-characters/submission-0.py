class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        freqT = {}
        freqS = {}
        for c in t:
            freqT[c] = freqT.get(c,0) + 1
            freqS[c] = 0
        ans = s
        have = 0
        need = len(freqT)
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in freqS:
                freqS[c] += 1
                if freqS[c] == freqT[c]:
                    have += 1
            while have == need:
                if r-l+1 < len(ans):
                    ans = s[l:r+1]
                if s[l] in freqS:
                    freqS[s[l]] -= 1
                    if freqS[s[l]] < freqT[s[l]]:
                        have -= 1
                l+=1

        return ans
