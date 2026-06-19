class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for word in strs:
            encoding+= "$" + str(len(word)) + word
        return encoding

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            print(s[i], decoded)
            length = int(s[i+1])
            decoded.append(s[i+2:i+2+length])
            i = i+2+length
        return decoded