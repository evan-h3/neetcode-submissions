class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for word in strs:
            encoding+= str(len(word)) + "$" + word
        return encoding

    def decode(self, s: str) -> List[str]:
        decoded = []
        l,r = 0, 0
        while r < len(s):
            while s[r+1] != "$":
                r+=1
            length = int(s[l:r+1])
            decoded.append(s[r+2:r+2+length])
            l = r+1+length
        return decoded