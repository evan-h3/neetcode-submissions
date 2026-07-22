class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            visiting = set()
            for j in range(i, len(s)):
                if s[j] in visiting:
                    break
                visiting.add(s[j])
                max_len = max(max_len, len(visiting))
        return max_len