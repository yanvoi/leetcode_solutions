class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        operators = {'+', '-', '*', '/'}
        
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            val2 = stack.pop()
            val1 = stack.pop()

            if token == '+':
                stack.append(val1 + val2)
            elif token == '-':
                stack.append(val1 - val2)
            elif token == '*':
                stack.append(val1 * val2)
            else:
                # this solves the problem of negative numbers being
                # truncated to smaller numbers
                stack.append(int(float(val1 / val2)))

        return stack.pop()
        
