class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += '#' + str(len(s)) + s
        return encoded

        #5bobby
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                length = int(s[i+1])
                i+=1
                decoded.append(s[i+1:i+1+length])
            else:
                i+=1
        return decoded
