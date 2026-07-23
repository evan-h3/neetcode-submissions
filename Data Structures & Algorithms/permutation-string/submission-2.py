class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        freq1 = Counter(s1)
        for i in range(len(s2)):
            freq2 = {}
            for j in range(i, len(s2)):
                freq2[s2[j]] = freq2.get(s2[j],0)+1
                if freq1 == freq2:
                    return True
        return False

                