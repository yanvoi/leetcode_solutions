# first take care of * and / whenever needed
# then add and subtract alternately the numbers left on the stack
class Solution:
    def clumsy(self, n: int) -> int:
        
        operations = ["*", "/", "+", "-"]
        stack = []
        operation = -1

        for num in range(n, 0, -1):
            stack.append(num)
            if operations[operation%4] in "*/":
                a = stack.pop()
                b = stack.pop()
                if operations[operation%4] == "*":
                    stack.append(a*b)
                else:
                    stack.append(b // a)
            operation += 1

        return stack[0] + sum(num if i % 2 == 0 else -num for i, num in enumerate(stack[1:]))
