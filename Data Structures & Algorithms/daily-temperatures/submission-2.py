class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            curr = temperatures[i]
            while stack and curr > stack[-1][0]:
                    _, prev_i = stack.pop()
                    res[prev_i] = i-prev_i
            stack.append((curr,i))
        return res
                