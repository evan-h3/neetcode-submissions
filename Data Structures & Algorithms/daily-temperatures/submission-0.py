class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                top = stack.pop()
                ans[top[1]] = i-top[1]
            stack.append((val,i))
        return ans
            

