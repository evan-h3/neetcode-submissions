class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            length = len(word)
            string+=(str(length)+ "#" + word)
        return string
    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            j+=1
            length = int(s[i:j])
            ans.append(s[j+1:j+1+length])
            i = j + 1 + length
        return ans
