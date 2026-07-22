class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        res = 0
        l = 0

        for r in range(len(s)):
            freq[ord(s[r]) - ord('A')] += 1
            max_freq = max(freq)
            while (r-l+1) - max_freq > k:
                freq[ord(s[l]) - ord('A')]-=1
                l+=1
            res = max(res,r-l+1)

        return res