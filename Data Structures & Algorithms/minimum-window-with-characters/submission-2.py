class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        #initialize 
        #freq map for target s
        #have and need values to store satisfied letter
        #res and lenRes variables to hold index/length of smallest str
        freq_t = {}
        for l in t:
            freq_t[l] = freq_t.get(l,0) + 1
        
        have, need = 0, len(freq_t)

        res, lenRes = [-1,-1], float("infinity")

        l = 0
        freq_curr = {}
        #loop through string s and create seperate 
        #counter to hold freq of visiting letters
        for r in range(len(s)):
            # add to current freq and update have value if needed
            freq_curr[s[r]] = freq_curr.get(s[r],0) + 1
            if s[r] in freq_t and freq_curr[s[r]] == freq_t[s[r]]:
                have+=1
            
            #while we have what we need, update window to find smallest
            while have == need:
                if r-l+1 < lenRes:
                    res = [l,r]
                    lenRes = r-l+1

                freq_curr[s[l]] -= 1 #shrink window
                if s[l] in freq_t and freq_curr[s[l]] < freq_t[s[l]]:
                    have -= 1 #can decrement because have == need to enter loop
                l+=1
                
        l, r = res
        return s[l:r+1] if lenRes != float('infinity') else ""
                
        

