class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse = True)
        stack = []
        for p2, s2 in cars:
            if not stack:
                stack.append((p2,s2))
            else:
                p1 = stack[-1][0]
                s1 = stack[-1][1]
                if ((target - p1)/s1) < ((target-p2)/s2):
                    stack.append((p2,s2))
        return len(stack)

