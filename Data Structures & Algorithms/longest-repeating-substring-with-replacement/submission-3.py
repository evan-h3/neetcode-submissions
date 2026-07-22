class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 1
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('A')] += 1
                if j-i+1 - max(freq) <= k:
                    max_len = max(max_len, j-i+1)
        return max_len