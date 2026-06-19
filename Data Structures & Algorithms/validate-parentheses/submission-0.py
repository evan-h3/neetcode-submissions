class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        stack = []
        for b in s:
            if b in brackets:
                if stack and stack.pop() != brackets[b]:
                    return False
            else:
                stack.append(b)
        return True if not stack else False
