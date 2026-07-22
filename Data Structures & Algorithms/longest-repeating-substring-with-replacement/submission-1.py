class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 1
        for i in range(len(s)):
            replacements = k
            for j in range(i+1, len(s)):
                if s[j] != s[i]:
                    if replacements == 0:
                        break
                    replacements-=1
                max_len = max(max_len, j-i+1)
        return max_len