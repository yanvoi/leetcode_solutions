class Solution:
    def calculate(self, s: str) -> int:

        self.s = s
        return self.__calculate__(0)[0]


    def __calculate__(self, i):

        stack, sign, num = [], '+', 0
        while i < len(self.s):
            char = self.s[i]

            if char.isdigit():
                num = num*10 + int(char)
            elif char in '+-*/':
                self.__update_stack__(num, sign, stack)
                num, sign = 0, char
            elif char == '(':
                num, index = self.__calculate__(i + 1)
                i = index - 1
            elif char == ')':
                self.__update_stack__(num, sign, stack)
                return sum(stack), i + 1

            i += 1

        self.__update_stack__(num, sign, stack)
        return sum(stack), i


    def __update_stack__(self, val, operation, stack):
            if operation == '+':
                stack.append(val)
            elif operation == '-':
                stack.append(-val)
            elif operation == '*':
                stack.append(stack.pop() * val)
            else:
                stack.append(stack.pop() // val)
        
