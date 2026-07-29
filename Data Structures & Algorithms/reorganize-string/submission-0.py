class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        if max(freq.values()) > len(s)//2:
            return ""
        
        res = [""] * len(s)
        sorted_freq = sorted(list(freq.items()), key = lambda x:x[1], reverse="True")
        index = 0
        curr = 0

        for l, f in sorted_freq:
            for _ in range(f):
                res[index] = l
                index+=2
                if index > len(s)-1:
                    index = 1
                
        return "".join(res)
