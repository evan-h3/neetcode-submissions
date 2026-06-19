class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for i in range(len(strs)):
            freq = [0] * 26
            for c in strs[i]:
                freq[ord(c)-ord('a')] += 1
            freq = tuple(freq)
            if freq not in hashtable:
                hashtable[freq] = [strs[i]]
            else:
                hashtable[freq].append(strs[i])
        return list(hashtable.values())