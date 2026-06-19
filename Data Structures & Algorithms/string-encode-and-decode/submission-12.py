class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for w in strs:
            encoded = "" + str(len(w)) + "$" + w
            new_str += encoded
        return new_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            length = ""
            while s[i] != "$":
                length += s[i]
                i+=1
            print(s, length)
            length = int(length)
            w = s[i+1:i+length+1]
            ans.append(w)
            i+=length+1
        return ans
