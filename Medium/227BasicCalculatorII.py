class Solution:
    def calculate(self, s: str) -> int:

        stack, sign, num = [], '+', 0

        for i, char in enumerate(s):
            if char.isdigit():
                num = num*10 + int(char)
            
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    tmp = stack.pop()
                    if tmp // num < 0 and tmp % num != 0:
                        stack.append(tmp//num + 1)
                    else:
                        stack.append(tmp//num)

                sign = char
                num = 0

        return sum(stack)
