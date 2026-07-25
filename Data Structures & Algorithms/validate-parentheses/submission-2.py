class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { ')':'(',  ']':'[',  '}':'{'}
        stack = []
        for p in s:
            if stack and p in ')}]':
                if stack[-1] != mapping[p]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(p)
        return True if not stack else False