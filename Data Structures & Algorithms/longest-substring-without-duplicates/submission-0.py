class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        visiting = set()
        l = 0
        for r in range(len(s)):
            print(l,r, visiting)
            if s[r] in visiting:
                while s[l] != s[r]:
                    visiting.remove(s[l])
                    l+=1
                l+=1
            else:
                visiting.add(s[r])
            maxLen = max(maxLen, r-l+1)
        return maxLen


