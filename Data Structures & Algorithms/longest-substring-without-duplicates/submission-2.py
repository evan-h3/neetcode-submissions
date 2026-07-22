class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        visiting = set()
        l = 0
        for r in range(len(s)):
            while s[r] in visiting:
                visiting.remove(s[l])
                l+=1
            visiting.add(s[r])
            max_len = max(max_len, len(visiting))
        return max_len