class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack = []
        for n in num:
            while stack and stack[-1] > n and k:
                stack.pop()
                k -= 1

            if stack or n != '0':
                stack.append(n)

        # if we can still get rid of k digits then we get rid of the k right most ones
        if k:
            stack = stack[:-k]

        return ''.join(stack) if stack else '0'
