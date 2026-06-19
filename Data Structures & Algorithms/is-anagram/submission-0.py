class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = {}
        for c in s:
            S[c] = S.get(c,0) + 1
        T = {}
        for c in t:
            T[c] = T.get(c,0) + 1
        return S == T

