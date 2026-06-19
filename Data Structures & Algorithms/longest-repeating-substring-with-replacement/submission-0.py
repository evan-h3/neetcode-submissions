class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        most_freq = 0
        l = 0
        max_length = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1
            most_freq = max(most_freq, max(freq.values()))
            while (r-l+1 - most_freq) > k:
                    freq[s[l]] -= 1
                    l += 1
                    most_freq = max(most_freq, max(freq.values()))
            max_length = max(max_length, r-l+1)
        return max_length


