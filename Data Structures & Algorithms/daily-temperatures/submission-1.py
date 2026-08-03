class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            curr = temperatures[i]
            for j in range(i,len(temperatures)):
                next = temperatures[j]
                if next>curr:
                    res[i] = (j-i)
                    break
        return res
                