class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                val = stack.pop()
                stack[-1] += val
            elif t == '-':
                val = stack.pop()
                stack[-1] -= val
            elif t == '*':
                val = stack.pop()
                stack[-1] *= val
            elif t == '/':
                val = stack.pop()
                stack[-1] = int(stack[-1] / val)
            else:
                stack.append(int(t))

        return stack[0]

        
                
